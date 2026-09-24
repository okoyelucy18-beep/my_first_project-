from pathlib import Path

root = Path(r"c:\Users\Ebube\Desktop\discovery\Discover\templates")
root.mkdir(parents=True, exist_ok=True)

layout = '''{% load static %}
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{% block title %}{{ page_title|default:site_name }}{% endblock %}</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = { theme: { extend: { colors: { monastery: '#1f2937', gold: '#d4a64f' } } } }
  </script>
</head>
<body class="bg-stone-100 text-slate-800">
  <header class="bg-stone-900 text-white shadow">
    <div class="max-w-6xl mx-auto px-4 py-4 flex flex-col gap-3 md:flex-row md:items-center md:justify-between">
      <div>
        <a href="{% url 'home' %}" class="text-2xl font-serif tracking-wide">{{ site_name }}</a>
        <p class="text-xs uppercase tracking-[0.3em] text-amber-300">{{ region_name }}</p>
      </div>
      <nav class="flex flex-wrap gap-3 text-sm">
        <a class="hover:text-amber-300" href="{% url 'home' %}">Home</a>
        {% for monastery in nav_monasteries %}
          <a class="hover:text-amber-300" href="{{ monastery.get_absolute_url }}">{{ monastery.name }}</a>
        {% endfor %}
        <a class="hover:text-amber-300" href="{% url 'retreats' %}">Retreats</a>
        <a class="hover:text-amber-300" href="{% url 'guidelines' %}">Guidelines</a>
        <a class="hover:text-amber-300" href="{% url 'prayer-intentions' %}">Intentions</a>
      </nav>
    </div>
  </header>

  {% if messages %}
    <div class="max-w-6xl mx-auto px-4 pt-4">
      {% for message in messages %}
        <div class="mb-2 rounded border px-3 py-2 {% if message.tags == 'error' %}bg-red-50 border-red-200 text-red-700{% else %}bg-emerald-50 border-emerald-200 text-emerald-700{% endif %}">
          {{ message }}
        </div>
      {% endfor %}
    </div>
  {% endif %}

  <main class="min-h-screen">
    {% block content %}{% endblock %}
  </main>

  <footer class="bg-stone-900 text-stone-200 mt-12">
    <div class="max-w-6xl mx-auto px-4 py-8 text-sm flex flex-col md:flex-row md:justify-between gap-3">
      <p>© 2026 Discover Monasteries. Sacred sanctuaries of Anambra State.</p>
      <div class="flex gap-4 flex-wrap">
        <a href="{% url 'home' %}" class="hover:text-amber-300">Home</a>
        <a href="{% url 'retreats' %}" class="hover:text-amber-300">Retreats</a>
        <a href="{% url 'guidelines' %}" class="hover:text-amber-300">Guidelines</a>
      </div>
    </div>
  </footer>
</body>
</html>
'''

home = '''{% extends 'layout.html' %}
{% block title %}{{ page_title|default:'Discover Monasteries' }}{% endblock %}

{% block content %}
<section class="bg-gradient-to-r from-stone-900 via-stone-800 to-amber-900 text-white">
  <div class="max-w-6xl mx-auto px-4 py-20">
    <p class="text-xs uppercase tracking-[0.35em] text-amber-300">Anambra Sacred Sanctuaries</p>
    <h1 class="mt-4 text-4xl md:text-6xl font-serif leading-tight">Seek solitude, encounter the divine.</h1>
    <p class="mt-5 max-w-2xl text-lg text-stone-200">Discover contemplative monasteries, prayerful retreats, and sacred spaces in Anambra State, Nigeria.</p>
    <div class="mt-8 flex flex-wrap gap-4">
      <a href="#monasteries" class="bg-amber-400 text-stone-900 px-5 py-3 rounded font-semibold">Explore monasteries</a>
      <a href="{% url 'retreats' %}" class="border border-white/30 px-5 py-3 rounded text-white">Plan a retreat</a>
    </div>
  </div>
</section>

<section id="monasteries" class="max-w-6xl mx-auto px-4 py-16">
  <div class="mb-8">
    <p class="text-xs uppercase tracking-[0.3em] text-amber-700">Monastic Directory</p>
    <h2 class="mt-2 text-3xl font-serif">Three consecrated havens</h2>
  </div>

  <div class="grid md:grid-cols-3 gap-6">
    {% for monastery in monasteries %}
      <article class="bg-white rounded-xl shadow overflow-hidden border border-stone-200">
        <div class="h-48 bg-cover bg-center" style="background-image: url('{{ monastery.image_url|default:'https://images.unsplash.com/photo-1507692049790-de58290a4334' }}');"></div>
        <div class="p-6">
          <p class="text-xs uppercase tracking-[0.25em] text-amber-700">{{ monastery.order_name|default:'Monastic Community' }}</p>
          <h3 class="mt-3 text-2xl font-serif text-stone-900">{{ monastery.name }}</h3>
          <p class="mt-3 text-sm text-stone-600">{{ monastery.location }}</p>
          <p class="mt-4 text-stone-700">{{ monastery.summary }}</p>
          <a href="{{ monastery.get_absolute_url }}" class="inline-block mt-5 text-amber-700 font-semibold">Visit sanctuary →</a>
        </div>
      </article>
    {% empty %}
      <p>No monasteries are available yet.</p>
    {% endfor %}
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 pb-16 grid lg:grid-cols-2 gap-8">
  <div class="bg-white p-8 rounded-xl shadow border border-stone-200">
    <p class="text-xs uppercase tracking-[0.25em] text-amber-700">Prayer intentions</p>
    <h3 class="mt-2 text-2xl font-serif">Entrust a prayer</h3>
    <form method="post" action="{% url 'submit_prayer_intention' %}" class="mt-5 space-y-4">
      {% csrf_token %}
      {{ prayer_form.as_p }}
      <button type="submit" name="submit_prayer" class="bg-stone-900 text-white px-5 py-3 rounded">Submit intention</button>
    </form>
  </div>

  <div class="bg-stone-900 text-white p-8 rounded-xl shadow">
    <p class="text-xs uppercase tracking-[0.25em] text-amber-300">Retreat booking</p>
    <h3 class="mt-2 text-2xl font-serif">Request a visit</h3>
    <form method="post" action="{% url 'submit_retreat_request' %}" class="mt-5 space-y-4 text-stone-900">
      {% csrf_token %}
      {{ retreat_form.as_p }}
      <button type="submit" name="submit_retreat" class="bg-amber-400 text-stone-900 px-5 py-3 rounded font-semibold">Send request</button>
    </form>
  </div>
</section>
{% endblock %}
'''

monastery_detail = '''{% extends 'layout.html' %}
{% block title %}{{ monastery.name }}{% endblock %}

{% block content %}
<section class="bg-gradient-to-r from-stone-900 via-stone-800 to-amber-900 text-white">
  <div class="max-w-6xl mx-auto px-4 py-20">
    <p class="text-xs uppercase tracking-[0.35em] text-amber-300">{{ monastery.order_name }}</p>
    <h1 class="mt-4 text-4xl md:text-6xl font-serif leading-tight">{{ monastery.name }}</h1>
    <p class="mt-4 max-w-2xl text-lg text-stone-200">{{ monastery.summary }}</p>
    <div class="mt-8 flex flex-wrap gap-4 text-sm">
      <span class="bg-white/10 px-3 py-2 rounded">{{ monastery.location }}</span>
      <span class="bg-white/10 px-3 py-2 rounded">{{ monastery.region }}</span>
    </div>
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 py-16 grid lg:grid-cols-2 gap-10">
  <div>
    <img src="{{ monastery.image_url|default:'https://images.unsplash.com/photo-1507692049790-de58290a4334' }}" alt="{{ monastery.name }}" class="w-full h-80 object-cover rounded-xl shadow" />
  </div>
  <div class="space-y-6">
    <div>
      <p class="text-xs uppercase tracking-[0.25em] text-amber-700">About the monastery</p>
      <p class="mt-3 text-lg text-stone-700">{{ monastery.description }}</p>
    </div>
    <div>
      <p class="text-xs uppercase tracking-[0.25em] text-amber-700">Directions</p>
      <p class="mt-3 text-stone-700">{{ monastery.directions|default:'Ask for the monastery gate or main cloister at the local parish junction.' }}</p>
    </div>
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 pb-16 grid lg:grid-cols-2 gap-8">
  <div class="bg-white p-8 rounded-xl shadow border border-stone-200">
    <p class="text-xs uppercase tracking-[0.25em] text-amber-700">Visitor guidelines</p>
    <ul class="mt-5 space-y-3 text-stone-700 list-disc list-inside">
      <li>Dress modestly and keep phone volume low.</li>
      <li>Respect silence in the chapel and cloister areas.</li>
      <li>Follow the monastery bell schedule and guestmaster instructions.</li>
      <li>Do not enter enclosed living quarters without permission.</li>
    </ul>
  </div>

  <div class="bg-stone-900 text-white p-8 rounded-xl shadow">
    <p class="text-xs uppercase tracking-[0.25em] text-amber-300">Submit an intention</p>
    <form method="post" action="{% url 'submit_prayer_intention' %}" class="mt-5 space-y-4 text-stone-900">
      {% csrf_token %}
      {{ prayer_form.as_p }}
      <button type="submit" name="submit_prayer" class="bg-amber-400 text-stone-900 px-5 py-3 rounded font-semibold">Send prayer</button>
    </form>
  </div>
</section>
{% endblock %}
'''

root.joinpath('layout.html').write_text(layout, encoding='utf-8')
root.joinpath('home.html').write_text(home, encoding='utf-8')
root.joinpath('monastery_detail.html').write_text(monastery_detail, encoding='utf-8')
root.joinpath('dit.html').write_text('''{% extends "layout.html" %}\n{% block content %}\n<section class="max-w-6xl mx-auto px-4 py-16">\n  <div class="bg-white rounded-xl shadow border border-stone-200 p-8">\n    <p class="text-xs uppercase tracking-[0.25em] text-amber-700">Visitor information</p>\n    <h1 class="mt-2 text-4xl font-serif">This monastery guide is ready for the next content section.</h1>\n    <p class="mt-4 text-stone-700">Use this view for retreat guidance, visitor rules, and living monastic details.</p>\n  </div>\n</section>\n{% endblock %}\n''', encoding='utf-8')

print('templates written')
