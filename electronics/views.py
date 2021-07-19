from django.shortcuts import render,HttpResponse
import turicreate as tc
from django.templatetags.static import static



electronics = tc.SFrame.read_csv('./static/electronics.csv')
users = electronics["user_id"].unique()
category_image={'Portable Audio & Video':"/electronics/portable_audio.jpg",
                'Computers & Accessories':"/electronics/computer_accesory.jpg",
                'Home Audio':"/electronics/home_audio.jpg",
                'Accessories & Supplies':"/electronics/accessories_and_supply.jpg",
                'Camera & Photo':"/electronics/camera_and_photo.jpg",
                'Television & Video':"/electronics/television_and_video.jpg",
                'Security & Surveillance':"/electronics/security.jpg",
                'Wearable Technology':"/electronics/wearable.jpg",
                'Headphones':"/electronics/headphones.jpg",
                'Car Electronics & GPS':"/electronics/car.jpg"}

# Create your views here.
def electronics_recommender(request):
    products=[]
    if request.method == 'GET':
        return render(request, 'electronics_recommendation.html',{"products":products,"users":users[:200]})
    if request.method == 'POST':
        model=tc.load_model("./static/electronics_recommender/")
        userid=request.POST['userid']
        print("hey")
        print(userid)
        recommended_items=model.recommend(users=[userid])
        print(recommended_items)
        items_recommended= recommended_items["item_id"]
        # return HttpResponse(items_recommended)
        for item in items_recommended[:5]:
            category=electronics[electronics["item_id"]==item]["category"][0]
            brand=electronics[electronics["item_id"]==item]["brand"][0]  
            image=category_image[category]
            products.append({"category":category,"brand":brand,"image":image})
        return render(request,'electronics_recommendation.html',{"products":products,"users":users[:200]})
        

# Create your views here.

    
