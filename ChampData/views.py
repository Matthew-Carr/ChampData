from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from ChampData.models import Champion

def index(request):
	champion_list = []
	for champ in Champion.objects.order_by('name'):
		if ' ' in champ.name:
			champion_list.append(champ.name.replace(' ', '_'))
		elif "'" in champ.name:
			champion_list.append(champ.name.replace("'", '_'))
		elif "." in champ.name:
			champion_list.append(champ.nam.replace(".", ''))
	 	else:
			champion_list.append(champ.name)

	#champion_list = Champion.objects.order_by('name')
	context = {'champion_list': champion_list}
	return render(request, 'ChampData/base.html', context)

def compare(request, champion1, champion2):
	format_champion1 = champion1[0].upper() + champion1[1:].lower()
	format_champion2 = champion2[0].upper() + champion2[1:].lower()
	champion1_requested = get_object_or_404(Champion, name=format_champion1)
	champion2_requested = get_object_or_404(Champion, name=format_champion2)
	difference = []	

	list1 = Champion.objects.values_list('hp', 'hpPlus', 'hp5', 'hp5Plus','mp', 'mpPlus', 'mp5', 'mp5Plus', 'ad', 'adPlus', 'aSpeed', 'asPlus', 'ar', 'arPlus', 'mr', 'mrPlus', 'ms', 'adRange').filter(name=format_champion1)
	list2 = Champion.objects.values_list('hp', 'hpPlus', 'hp5', 'hp5Plus','mp', 'mpPlus', 'mp5', 'mp5Plus', 'ad', 'adPlus', 'aSpeed', 'asPlus', 'ar', 'arPlus', 'mr', 'mrPlus', 'ms', 'adRange').filter(name=format_champion2)

	for i in xrange(len(list1[0])):
		#if isinstance(list1[i], (int, float, long, complex)):
		difference.append(float(list1[0][i]) - float(list2[0][i]))

	
	context = {'champion1': champion1_requested,
		   'champion2': champion2_requested,
		   'difference': difference}
        
	return render(request, 'ChampData/compare.html', context)

def detail(request, champion):
	format_champion = champion[0].upper() + champion[1:].lower()
	champion_requested = get_object_or_404(Champion, name=format_champion)
	image_url = "ChampData/images/" + champion_requested.name + "_OriginalLoading.jpg"

	context = {'image_url': image_url,
		   'champion_name': champion_requested.name,
		   'hp': champion_requested.hp,
		   'hpPlus': champion_requested.hpPlus,
		   'hp5': champion_requested.hp5,
		   'hp5Plus': champion_requested.hp5Plus,
		   'mp': champion_requested.mp,
		   'mpPlus': champion_requested.mpPlus,
		   'mp5': champion_requested.mp5,
		   'mp5Plus': champion_requested.mp5Plus,
		   'ad': champion_requested.ad,
		   'adPlus': champion_requested.adPlus,
		   'as': champion_requested.aSpeed,
		   'asPlus': champion_requested.asPlus,
		   'ar': champion_requested.ar,
		   'arPlus': champion_requested.arPlus,
		   'mr': champion_requested.mr,
		   'mrPlus': champion_requested.mrPlus,
		   'ms': champion_requested.ms,
		   'range': champion_requested.adRange
	}
	
	return render(request, 'ChampData/ChampDetails.html', context)


















