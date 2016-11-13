#Лазченко Влад. ВИС22. Лабораторная работа 6. VK API "VKPhotosGeoLocation"
 
import vk
print('VK Photos geo location')
session = vk.Session('d3e2557b997e7a9b28c8a451dbef53bc23c54158456a2f36886883a3649e32a4f84f2003ad3990dc790c4')
api = vk.API(session)
friends = api.friends.get()
print(len(friends))
print(friends)
friend_info = api.users.get(user_ids=friends)
for friend in friend_info:
    print('ID: %s Name: %s %s' % (friend['uid'], friend['last_name'], friend['first_name']))
    for id in friends:
        print('Receive information user: %s' % id)
        albums = api.photos.getAlbum(owner_id=id)
        print('\t...albums %s...' % len(albums))
        for album in albums:
            try:
                photos = api.photos.get(owner_id=id, album_id=album['aid'])
                print('\t\t...Obrabatyvaem photographii alboma...')
                for photo in photos:
                    if 'lat' in photo and 'long' in photo:
                        geolocation.append((photo['lat'], photo['long']))
                        print('\t\t...naideno %s photo' % len(photos))
            except:
                pass
            time.sleep(0.5)
        time.sleep(0.5)
        js_code = ''
        for loc in geolocation:
            js_code += 'new google.maps.Marker({ position: {lat: %s, lng: %s}, map: map});\n' % (loc[0], loc[1])
html = open('map.html').read()
html = html.replace('/* PLACEHOLDER */', js_code)
f = open('VKPhotosGeoLocation.html', 'w')
f.write(html)
f.close()
 
