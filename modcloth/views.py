from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
import turicreate as tc
from django.templatetags.static import static



modcloth = tc.SFrame.read_csv('./static/modcloth.csv')
users = modcloth["user_id"].unique()
category_image={'Dresses':"/modcloth/dresses.jpg",
                'Outerwear':"/modcloth/outerwear.jpg",
                'Bottoms':"/modcloth/bottoms.jpg",
                'Tops':"/modcloth/tops.jpg",}

# Create your views here.
def modcloth_recommender(request):
    products=[]
    if request.method == 'GET':
        return render(request, 'mc.html',{"products":products,"users":users[:200]})
    if request.method == 'POST':
        model=tc.load_model("./static/modcloth_recommender/")
        userid=request.POST['userid']
        recommended_items=model.recommend(users=[userid])
        print(recommended_items)
        items_recommended= recommended_items["item_id"]
        for item in items_recommended[:5]:
            category=modcloth[modcloth["item_id"]==item]["category"][0]
            brand=modcloth[modcloth["item_id"]==item]["brand"][0]  
            image=category_image[category]
            products.append({"category":category,"brand":brand,"image":image})
        return render(request,'mc.html',{"products":products,"users":users[:200]})
        

# Create your views here.

    

