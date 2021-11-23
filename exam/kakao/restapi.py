import requests


city = 'Dallas'
# Write your code here
pagenumber = 1
best_score = 0
food_outlets = []
answer = []
print(city)
while True:
    url = f'https://jsonmock.hackerrank.com/api/food_outlets?city={city}&page={pagenumber}'
    response = requests.get(url = url)    
    data = response.json()
    print(data)
    if data['total_pages'] < pagenumber:
        break
    
    for outlet in data['data']:
        outlet_rating = outlet['user_rating']['average_rating']
        outlet_name = outlet['name']
        if best_score < outlet_rating:
            best_score = outlet_rating
        food_outlets.append([outlet_name, outlet_rating, outlet['id']]) 
    pagenumber += 1
print(len(food_outlets))
id_list= []
for name, rating, id in food_outlets:
    print(name, rating)
    if rating == best_score and id not in id_list:
        answer.append(name)
        id_list.append(id)
print(answer)