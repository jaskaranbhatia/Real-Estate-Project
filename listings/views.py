from django.shortcuts import render,get_object_or_404
from .models import Listing
from .choice import bedroom_choices,price_choices,state_choices 
import requests
 
listings=Listing.objects.all()
def index(request):
	return render(request , 'listings.html', {
	'listings':listings
})
def listing(request,listing_id):
		instance = Listing.objects.filter(id=listing_id).values('city')[0]
		city = instance['city']
		location=city
		instance1 = Listing.objects.filter(id=listing_id).values('bedrooms')[0]
		bedrooms = instance1['bedrooms']
		bhk=bedrooms
		instance2 = Listing.objects.filter(id=listing_id).values('bathrooms')[0]
		bathrooms = instance2['bathrooms']
		bath=bathrooms
		instance3 = Listing.objects.filter(id=listing_id).values('sqft')[0]
		sqft = instance3['sqft']
		total_sqft=sqft
		print(location,bhk,bath,total_sqft)
		params={'location':location,
				'bhk':bhk,
				'bath':bath,
				'total_sqft':total_sqft
				}
		print(params)
		res=requests.post('https://realestate-restapi.herokuapp.com/predict_home_price',data=params)
		print(res.status_code)
		if res.status_code==200:
			data1=res.json()
			listing=get_object_or_404(Listing,pk=listing_id)
			return render(request , 'listing.html' ,{
				'price': data1['estimated_price'],
				'listing':listing
			})
def search(request):
	query_list=Listing.objects.all()
	locations=["1st block jayanagar", "1st phase jp nagar", "2nd phase judicial layout", "2nd stage nagarbhavi", "5th block hbr layout", "5th phase jp nagar", "6th phase jp nagar", "7th phase jp nagar", "8th phase jp nagar", "9th phase jp nagar", "aecs layout", "abbigere", "akshaya nagar", "ambalipura", "ambedkar nagar", "amruthahalli", "anandapura", "ananth nagar", "anekal", "anjanapura", "ardendale", "arekere", "attibele", "beml layout", "btm 2nd stage", "btm layout", "babusapalaya", "badavala nagar", "balagere", "banashankari", "banashankari stage ii", "banashankari stage iii", "banashankari stage v", "banashankari stage vi", "banaswadi", "banjara layout", "bannerghatta", "bannerghatta road", "basavangudi", "basaveshwara nagar", "battarahalli", "begur", "begur road", "bellandur", "benson town", "bharathi nagar", "bhoganhalli", "billekahalli", "binny pete", "bisuvanahalli", "bommanahalli", "bommasandra", "bommasandra industrial area", "bommenahalli", "brookefield", "budigere", "cv raman nagar", "chamrajpet", "chandapura", "channasandra", "chikka tirupathi", "chikkabanavar", "chikkalasandra", "choodasandra", "cooke town", "cox town", "cunningham road", "dasanapura", "dasarahalli", "devanahalli", "devarachikkanahalli", "dodda nekkundi", "doddaballapur", "doddakallasandra", "doddathoguru", "domlur", "dommasandra", "epip zone", "electronic city", "electronic city phase ii", "electronics city phase 1", "frazer town", "gm palaya", "garudachar palya", "giri nagar", "gollarapalya hosahalli", "gottigere", "green glen layout", "gubbalala", "gunjur", "hal 2nd stage", "hbr layout", "hrbr layout", "hsr layout", "haralur road", "harlur", "hebbal", "hebbal kempapura", "hegde nagar", "hennur", "hennur road", "hoodi", "horamavu agara", "horamavu banaswadi", "hormavu", "hosa road", "hosakerehalli", "hoskote", "hosur road", "hulimavu", "isro layout", "itpl", "iblur village", "indira nagar", "jp nagar", "jakkur", "jalahalli", "jalahalli east", "jigani", "judicial layout", "kr puram", "kadubeesanahalli", "kadugodi", "kaggadasapura", "kaggalipura", "kaikondrahalli", "kalena agrahara", "kalyan nagar", "kambipura", "kammanahalli", "kammasandra", "kanakapura", "kanakpura road", "kannamangala", "karuna nagar", "kasavanhalli", "kasturi nagar", "kathriguppe", "kaval byrasandra", "kenchenahalli", "kengeri", "kengeri satellite town", "kereguddadahalli", "kodichikkanahalli", "kodigehaali", "kodigehalli", "kodihalli", "kogilu", "konanakunte", "koramangala", "kothannur", "kothanur", "kudlu", "kudlu gate", "kumaraswami layout", "kundalahalli", "lb shastri nagar", "laggere", "lakshminarayana pura", "lingadheeranahalli", "magadi road", "mahadevpura", "mahalakshmi layout", "mallasandra", "malleshpalya", "malleshwaram", "marathahalli", "margondanahalli", "marsur", "mico layout", "munnekollal", "murugeshpalya", "mysore road", "ngr layout", "nri layout", "nagarbhavi", "nagasandra", "nagavara", "nagavarapalya", "narayanapura", "neeladri nagar", "nehru nagar", "ombr layout", "old airport road", "old madras road", "padmanabhanagar", "pai layout", "panathur", "parappana agrahara", "pattandur agrahara", "poorna pragna layout", "prithvi layout", "r.t. nagar", "rachenahalli", "raja rajeshwari nagar", "rajaji nagar", "rajiv nagar", "ramagondanahalli", "ramamurthy nagar", "rayasandra", "sahakara nagar", "sanjay nagar", "sarakki nagar", "sarjapur", "sarjapur  road", "sarjapura - attibele road", "sector 2 hsr layout", "sector 7 hsr layout", "seegehalli", "shampura", "shivaji nagar", "singasandra", "somasundara palya", "sompura", "sonnenahalli", "subramanyapura", "sultan palaya", "tc palaya", "talaghattapura", "thanisandra", "thigalarapalya", "thubarahalli", "thyagaraja nagar", "tindlu", "tumkur road", "ulsoor", "uttarahalli", "varthur", "varthur road", "vasanthapura", "vidyaranyapura", "vijayanagar", "vishveshwarya layout", "vishwapriya layout", "vittasandra", "whitefield", "yelachenahalli", "yelahanka", "yelahanka new town", "yelenahalli", "yeshwanthpur"]

	if 'keywords' in request.GET:
	    keywords = request.GET['keywords']
	    if keywords:
	      query_list = query_list.filter(description__icontains=keywords)

	if 'city' in request.GET:
	    city = request.GET['city']
	    if city:
	      query_list = query_list.filter(city__iexact=city)

	if 'state' in request.GET:
	    state = request.GET['state']
	    if state:
	      query_list = query_list.filter(state__iexact=state)

	if 'bedrooms' in request.GET:
	    bedrooms = request.GET['bedrooms']
	    if bedrooms:
	      query_list = query_list.filter(bedrooms__lte=bedrooms)

	



	if 'price' in request.GET:
	    price = request.GET['price']
	    if price:
	      query_list = query_list.filter(price__lte=price)

	return render(request , 'search.html',{
	'listings':query_list,
	'bedroom_choices':bedroom_choices,
	'price_choices':price_choices,	
	'state_choices':state_choices,
	'values':request.GET,
	'locations':locations
	})

def predict(request):
	if request.method=="POST":
		print("hello")
		location=request.POST['location']
		bhk=request.POST['bhk']
		bath=request.POST['bath']
		total_sqft=request.POST['total_sqft']

		location1=location
		print(location1)
		print(request.POST['location'])
		params={'location':location,
				'bhk':bhk,
				'bath':bath,
				'total_sqft':total_sqft
				}
		print(params)
		res=requests.post('https://realestate-restapi.herokuapp.com/predict_home_price',data=params)
		
		print(res.status_code)
		if res.status_code==200:
			data=res.json()
			return render(request,'predict.html',{
					'price': data['estimated_price'],
					'location1':request.POST['location'],
					'bhk1':request.POST['bhk'],
					'bath1':request.POST['bath'],
					'total_sqft1':request.POST['total_sqft']
				})

		else:
			return render(request,'predict.html',{
					'location':location,
					'bhk':bhk,
					'bath':bath,
					'total_sqft':total_sqft
				})
	else:
		return render(request,'predict.html',{
					'location':location,
					'bhk':bhk,
					'bath':bath,
					'total_sqft':total_sqft
				})