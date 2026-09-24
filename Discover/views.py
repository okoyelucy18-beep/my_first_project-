from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, render
from .forms import PrayerIntentForm, RetreatRequestForm
from .models import Monastery


def _site_context(extra_context=None):
    context = {
        'site_name': 'Discover Monasteries',
        'region_name': 'Anambra Sacred Sanctuaries',
        'navigation': (
            ('Sanctuaries', 'home'),
            ('Plan a retreat', 'retreats'),
            ('Visitor guide', 'guidelines'),
            ('Prayer intentions', 'prayer-intentions'),
        ),
        'nav_monasteries': Monastery.objects.filter(is_published=True).order_by('name'),
    }
    if extra_context:
        context.update(extra_context)
    return context


def _get_monastery_or_redirect(slug):
    monastery = Monastery.objects.filter(is_published=True, slug=slug).first()
    if not monastery:
        return None
    return monastery


def home(request):
    monasteries = Monastery.objects.filter(is_published=True).order_by('name')
    prayer_form = PrayerIntentForm()
    retreat_form = RetreatRequestForm()
    search = request.GET.get("q", "").strip()
    location = request.GET.get("location", "").strip()
    order = request.GET.get("order", "").strip()


    if request.method == 'POST' and 'submit_prayer' in request.POST:
        prayer_form = PrayerIntentForm(request.POST)
        if prayer_form.is_valid():
            prayer_form.save()
            messages.success(request, 'Your prayer intention has been received by the monastic community.')
            return redirect('home')

    if request.method == 'POST' and 'submit_retreat' in request.POST:
        retreat_form = RetreatRequestForm(request.POST)
        if retreat_form.is_valid():
            retreat_form.save()
            messages.success(request, 'Your retreat request has been submitted successfully.')
            return redirect('home')

        if search:
        monasteries = monasteries.filter(
            Q(name__icontains=search)
            | Q(location__icontains=search)
            | Q(order_name__icontains=search)
            | Q(short_description__icontains=search)
        )

    if location:
        monasteries = monasteries.filter(
            location__icontains=location
        )

    if order:
        monasteries = monasteries.filter(
            order_name__icontains=order
        )

    locations = (
        Monastery.objects
        .exclude(location="")
        .values_list("location", flat=True)
        .distinct()
        .order_by("location")
    )

    orders = (
        Monastery.objects
        .exclude(order_name="")
        .values_list("order_name", flat=True)
        .distinct()
        .order_by("order_name")
    )


    context = _site_context({
        'monasteries': monasteries,
        'prayer_form': prayer_form,
        'retreat_form': retreat_form,
        'page_title': 'Discover Monasteries', 
        'search': search,
        'location': location,
        'order': order,
        'locations': locations,
        'orders': orders,
    })
    return render(request, 'home.html', context)


def monastery_detail(request, slug):
    monastery = _get_monastery_or_redirect(slug)
    if not monastery:
        return redirect('home')

    context = _site_context({
        'monastery': monastery,
        'page_title': monastery.name,
        'prayer_form': PrayerIntentForm(initial={'monastery': monastery.id}),
        'retreat_form': RetreatRequestForm(initial={'monastery': monastery.id}),
    })
    return render(request, 'monastery_detail.html', context)


def holy_cross(request):
    monastery = _get_monastery_or_redirect('holy-cross-nteje')
    if not monastery:
        return redirect('home')
    context = _site_context({'monastery': monastery, 'page_title': monastery.name})
    return render(request, 'monastery_detail.html', context)


def st_benedict(request):
    monastery = _get_monastery_or_redirect('st-benedict-ozubulu')
    if not monastery:
        return redirect('home')
    context = _site_context({'monastery': monastery, 'page_title': monastery.name})
    return render(request, 'monastery_detail.html', context)


def carmelite(request):
    monastery = _get_monastery_or_redirect('carmelite-holy-family')
    if not monastery:
        return redirect('home')
    context = _site_context({'monastery': monastery, 'page_title': monastery.name})
    return render(request, 'monastery_detail.html', context)


def retreats(request):
    context = _site_context({'page_title': 'Plan a Sacred Retreat'})
    return render(request, 'monastery_detail.html', context)


def guidelines(request):
    context = _site_context({'page_title': 'Visitor Guidelines and Liturgy Hours'})
    return render(request, 'monastery_detail.html', context)


def prayer_intentions(request):
    context = _site_context({'page_title': 'Prayer Intentions'})
    return render(request, 'monastery_detail.html', context)


def submit_prayer_intention(request):
    if request.method != 'POST':
        return redirect('home')

    form = PrayerIntentForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your prayer intention was received with reverence.')
    else:
        messages.error(request, 'Please fix the errors in your prayer intention form.')
    return redirect('home')


def submit_retreat_request(request):
    if request.method != 'POST':
        return redirect('home')

    form = RetreatRequestForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your retreat request was submitted successfully.')
    else:
        messages.error(request, 'Please fix the errors in your retreat request form.')
    return redirect('home')
