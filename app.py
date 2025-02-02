import streamlit as st
from datetime import datetime
import os
import math

def check_availability(data):
    dayDate = datetime.now().date()
    for event_name, event_details in data.items():
        for x in event_details['genre']:
            if x == 'trending':
                sd_str = event_details.get('start_date')
                ed_str = event_details.get('end_date')
                sd = datetime.strptime(sd_str, "%Y-%m-%d").date()
                ed = datetime.strptime(ed_str, "%Y-%m-%d").date()
                if sd <= dayDate <= ed:
                    event_details['available'] = True


search_all_event = lambda x: [(key, value) for key, value in {**Riyadh_dict, **Jeddah_dict}.items() if x.lower() in key.lower()]


def getOptions(cities):
    listEvent = []
    for city in cities:
        listEvent.extend(eventType[city])
    return sorted(set(listEvent))


def filter_events_by_genre(selected_genres, dictionary):
    return {
        event_name: event_details
        for event_name, event_details in dictionary.items()
        if all(genre in event_details['genre'] for genre in selected_genres)
    }


def suggest_tourism_activity(selected_genres, Riyadh_dict, jeddah_dict):
    filtered_riyadh = filter_events_by_genre(selected_genres, Riyadh_dict) if Riyadh_checkbox else {}
    filtered_jeddah = filter_events_by_genre(selected_genres, jeddah_dict) if Jeddah_checkbox else {}

    all_filtered_events = {**filtered_riyadh, **filtered_jeddah}

    return all_filtered_events



Riyadh_dict = {
    'Leap 2025': {
        'genre': ['trending', 'tech'],
        'description': 'LEAP is an annual tech event that was founded in 2022 by the Ministry of Communication and Information Technology (Saudi Arabia) (MCIT), the Saudi Federation for Cybersecurity, Programming and Drones (SAFCSP) and Tahaluf, an Informa company.',
        'start_date': '2025-02-09',
        'end_date': '2025-02-12',
        'img': os.path.join('imgs', 'leap.png'),
        'available': False
    },
    'Porter House': {
        'genre': ['restaurant'],
        'description': 'PORTERHOUSE Restaurant Porter House is considered one of the best steak and meat restaurants in Riyadh. The restaurant is 100% Saudi. It was established in 2016. Children are only allowed until 7 pm.',
        'img': os.path.join('imgs', 'porter_house.jpg')
    },
    'Mama Noura': {
        'genre': ['restaurant'],
        'description': 'Mama Noura is your destination to savor the most delicious oriental and Arabic food in Riyadh, with dishes that reflect the distinctive and authentic taste of traditional Arabic food.',
        'img': os.path.join('imgs', 'mama_noura.jpg')
    },
    'The National Musem': {
        'genre': ['tourist attraction', 'historical'],
        'description': 'King Abdulaziz Historical Center (KAHC) is a cross-district heritage complex in Riyadh, Saudi Arabia, covering south of al-Murabba and north of al-Futah. Inaugurated in 1999, it includes several historic buildings and open green spaces that surround the Murabba Palace compound, which was the main residence and workplace of King Abdulaziz ibn Saud between 1938 and 1953.',
        'img': os.path.join('imgs', 'national_musem.jpg')
    },
    'Riyadh Zoo': {
        'genre': ['tourist attraction', 'zoo'],
        'description': 'Riyadh zoo is home to more than 1,300 animals from 190 species, which live in six protected areas.',
        'img': os.path.join('imgs', 'zoo.png')
    },
    'Boulevard City': {
        'genre': ['tourist attraction', 'restaurant', 'shopping', 'entertainment'],
        'description': 'Boulevard City contains gardens, dancing fountain, several cafes, local and global restaurants, shops for the most famous local and world brands, as well as many theatres for artistic and singing performances.',
        'img': os.path.join('imgs', 'city.jpeg')
    },
    'Taibah Market': {
        'genre': ['shopping', 'historical'],
        'description': "Souq Taibah is one of the oldest markets in Riyadh. Despite the sweep of modern commercial malls, it is still a main destination for the people of the city to purchase necessities, antiques, and many others, as the prices of its goods compete with the rest of the markets.",
        'img': os.path.join('imgs', 'souq-taibah.jpeg')
    },
    'Snow Village': {
        'genre': ['entertainment', 'trending'],
        'description': 'This place gives a good experience of snow games, fun and rides right in RIyadh. You don’t need any equipment to go there as they will provide you with a full gear for the adventure including gloves and an additional pair of socks.',
        'start_date': '2024-12-12',
        'end_date': '2025-02-02',
        'img': os.path.join('imgs', 'snow.jpg'),
        'price': 27,
        'available': False
    },
    'Saudi Cup 2025': {
        'genre': ['sports', 'trending'],
        'description': 'The world’s finest thoroughbreds and jockeys descend on King Abdulaziz Racecourse in Riyadh for Saudi Cup Weekend 2025 with prize money of over US$37.5M on offer. A celebration of the best Saudi sporting, entertainment, cuisine, and cultural experiences headlined by the World’s Richest Race, the Saudi Cup where US$20M is to be won. As the pinnacle of style, sophistication, and glamour, this is Riyadh’s social event of the year and a jewel in the crown of international racing.',
        'start_date': '2025-02-21',
        'end_date': '2025-02-22',
        'img': os.path.join('imgs', 'saudi_cup.png'),
        'price': 175,
        'available': False
    }
}

Jeddah_dict = {
    'AROYA Cruise': {
        'genre': ['trending', 'entertainment'],
        'description': 'The first ever remarkably Arabian cruise line, Our story began with an idea to offer our guests a vacation that is one of its kind, tailored to reflect the rich hospitality of the region that is unmatched anywhere in the world, to sail on an exceptional voyage in the red sea with an Arabian touch.',
        'start_date': '2024-12-16',
        'end_date': '2025-05-01',
        'img': os.path.join('imgs', 'aroya-cruises.jpg'),
        'price': 1350,
        'available': False
    },
    'Formula E': {
        'genre': ['trending', 'sports'],
        'description': 'the Kingdom of Saudi Arabia gets set to host another pair of races taking place on Friday 14 and Saturday 15 February 2025.',
        'start_date': '2025-02-14',
        'end_date': '2025-02-15',
        'img': os.path.join('imgs', 'formula.jpg'),
        'price': 70,
        'available': False
    },
    'Jeddah Park': {
        'genre': ['shopping'],
        'description': "Experience Jeddah Park's expansive space and impressive design with outdoor fountains and a sunlit high ceiling. Enjoy luxury shopping, cozy cafes, varied seating, a cinema, and a food court with options for all tastes. It also offers a children's entertainment area and nursery, ideal for families and friends.",
        'img': os.path.join('imgs', 'jeddah_park.jpg')
    },
    'Baco': {
        'genre': ['restaurant'],
        'description': 'Baco is a local concept that tells the story of Asian-Latin American Fusion Tapas told through Baos and Tacos with a unique dining experience and vibes.We celebrate the beauty of multi-cultural.',
        'img': os.path.join('imgs', 'baco.jpg')
    }
}



st.title('Tourism in Saudi Arabia')
search_word = st.text_input("Search", placeholder="Search for an event")
st.write("Choose the cities you want to visit:")

Riyadh_checkbox = st.checkbox("Riyadh")
Jeddah_checkbox = st.checkbox("Jeddah")

eventType = {
    "Riyadh": [genre for event in Riyadh_dict.values() for genre in event['genre']],
    "Jeddah": [genre for event in Jeddah_dict.values() for genre in event['genre']]
}




if Riyadh_checkbox and Jeddah_checkbox:
    selected_genres = st.multiselect("Select the event type", options=getOptions(["Riyadh", "Jeddah"]))
elif Riyadh_checkbox:
    selected_genres = st.multiselect("Select the event type", options=getOptions(["Riyadh"]))
elif Jeddah_checkbox:
    selected_genres = st.multiselect("Select the event type", options=getOptions(["Jeddah"]))

if st.button('Find event'):
    if selected_genres:
        suggested_events = suggest_tourism_activity(selected_genres, Riyadh_dict, Jeddah_dict)
        if suggested_events:
            check_availability(Riyadh_dict)
            check_availability(Jeddah_dict)
            num_columns = min(2, len(suggested_events))
            cols = st.columns(num_columns)

            for idx, (event_name, event_details) in enumerate(suggested_events.items()):
                col = cols[idx % num_columns]

                with col:
                    with st.container():
                        st.image(event_details['img'], caption=event_name)
                        st.subheader(event_name)
                        st.write(event_details['description'])
                        if 'available' in event_details:
                            st.write("Available to attend now:", "Yes" if event_details['available'] else "No")
        else:
            st.write("No events found with the selected criteria.")
    else:
        st.write("Please select at least one genre.")
        
        
if search_word:
    results = search_all_event(search_word)
    if results:
        check_availability(Riyadh_dict)
        check_availability(Jeddah_dict)
        
        # Create columns dynamically in pairs (2 columns)
        num_columns = min(2, len(results))
        cols = st.columns(num_columns)

        for i, (key, value) in enumerate(results):
            col = cols[i % num_columns]  # Determine which column (0 or 1) the current item goes into
            with col:
                st.header(key)
                st.image(value['img'])
                st.write(value["description"])
                if 'start_date' in value:
                    st.write("Start Date:", datetime.strptime(value["start_date"], "%Y-%m-%d").strftime("%B %d, %Y"))
                if 'end_date' in value:
                    st.write("End Date:", datetime.strptime(value["end_date"], "%Y-%m-%d").strftime("%B %d, %Y"))
                if 'price' in value:
                    st.write(f"Price: {value['price']}")
                st.write(f"Genre: {', '.join(value['genre'])}")
                if 'available' in value:
                    st.write("Can I attend this event today: ", "yes" if value['available'] else "no")
    else:
        st.write(f"No results found for '{search_word}'")
        
        
        
        
