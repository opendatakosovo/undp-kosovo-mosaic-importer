# -*- coding: utf-8 -*-

import csv
import os
from datetime import datetime, date
from slugify import slugify
from pymongo import MongoClient

# Connect to default local instance of mongo
client = MongoClient()

# Get database and collection
db = client.undpkosovomosaic
collection = db.mosaic
collection.remove({})

def parse():

    print "Importing UNDP KOSOVO MOSAIC DATA."

    with open('data/Mosaic-2012.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        line_number = 0
        next(csvfile)
        for row in reader:
            print line_number
            line_number = line_number + 1
            actual_problem = str(row[100])
            loud_noise = str(row[101])
            air_quality = str(row[102])
            can_problems_be_solved_by_local_authorities = str(row[103])
            ambulanta = str(row[104])
            hospital = str(row[105])
            local_comunity_office = str(row[106])
            municipal_office = str(row[107])
            shop = str(row[108])
            doctor = str(row[109])
            how_far_hospital = str(row[110])
            pharmacy = str(row[111])
            post_office = str(row[112])
            library = row[113]
            sports_centre = row[114]
            theatre = row[115]
            bank_atm = row[116]
            municipal_office = row[117]
            local_comunity_office = row[118]
            pre_school = row[119]
            primary_school = row[120]
            secondary_school = row[121]
            first_aid_emergency_services = row[122]
            fire_emergency_service = row[123]
            collections_completed_on_the_scheduled_day = row[124]
            solid_waste_collection_services = row[125]
            garbage_selection = row[126]
            management_of_land_fills = row[127]
            water_supply = row[128]
            sewage_and_sanitation = row[129]
            level_of_street_cleanliness = row[130]
            condition_of_streets = row[131]
            horizontal_and_vertical_signage = row[132]
            safety_security_of_parking = row[133]
            availability_of_public_parking_spaces = row[134]
            proper_signage_of_public_parking = row[135]
            location_of_public_parking_sports = row[136]
            availability_of_sidewalks = row[137]
            usability_of_sidewalks = row[138]
            condition_of_sidewalks = row[139]
            cleanliness_city = row[140]
            cleanliness_municipality = row[141]
            road_condition_city = row[142]
            road_condition_municipality = row[143]
            Q11_A = row[144]
            Q11_B = row[145]
            Q11_C = row[146]
            Q11_D = row[147]
            Q11_E = row[148]
            Q11_F = row[149]
            Q11_G = row[150]
            Q11_H = row[151]
            Q11_I = row[152]
            Q11_J = row[153]
            Q11_K = row[154]
            Q12_A = row[155]
            Q12_B = row[156]
            Q12_C = row[157]
            Q12_D = row[158]
            Q13_A = row[159]
            Q13_B = row[160]
            Q13_C = row[161]
            Q13_D = row[162]
            Q13_E = row[163]
            Q13_F = row[165]
            Q13_G = row[166]
            Q13_H = row[167]
            Q13_I = row[168]
            Q13_J = row[169]
            Q14 = row[170]
            Q15 = row[171]
            Q15a = row[172]
            Q16 = row[173]
            Q17 = row[174]
            Q18 = row[175]
            Q19 = row[176]
            Q20 = row[177]
            Q21 = row[178]
            Q22 = row[179]
            Q23 = row[180]
            Q24 = row[181]
            Q25 = row[182]
            Q26 = row[183]

            report = {
                "data": {
                    "problems_in_municipality": {
                        "actual_problem": actual_problem,
                        "loud_noise": loud_noise,
                        "air_quality": air_quality,
                        "can_problems_be_solved_by_local_authorities": can_problems_be_solved_by_local_authorities
                    },
                    "satisfaction_with_public_services": {
                        "visited_closest_facility": {
                            "ambulanta": ambulanta,
                            "hospital": hospital,
                            "local_comunity_office": local_comunity_office,
                            "municipal_office": municipal_office
                        },
                        "how_far_is_the_facility": {
                            "shop": shop,
                            "doctor": doctor,
                            "how_far_hospital": how_far_hospital,
                            "pharmacy": pharmacy,
                            "post_office": post_office,
                            "library": library,
                            "sports_centre": sports_centre,
                            "theatre": theatre,
                            "bank_atm": bank_atm,
                            "municipal_office": municipal_office,
                            "local_comunity_office": local_comunity_office,
                            "pre-school": pre_school,
                            "primary_school": primary_school,
                            "secondary_school": secondary_school
                        },
                        "satisfcation_with_services": {
                            "first_aid_emergency_services": first_aid_emergency_services,
                            "fire_emergency_service": fire_emergency_service,
                            "collections_completed_on_the_scheduled_day": collections_completed_on_the_scheduled_day,
                            "solid_waste_collection_services": solid_waste_collection_services,
                            "garbage_selection": garbage_selection,
                            "management_of_land_fills": management_of_land_fills,
                            "water_supply ": water_supply,
                            "sewage_and_sanitation": sewage_and_sanitation,
                            "streets": {
                                "level_of_street_cleanliness": level_of_street_cleanliness,
                                "condition_of_streets": condition_of_streets,
                                "horizontal_and_vertical_signage": horizontal_and_vertical_signage
                            },
                            "public_parking": {
                                "safety_security_of_parking": safety_security_of_parking,
                                "availability_of_public_parking_spaces": availability_of_public_parking_spaces,
                                "proper_signage_of_public_parking": proper_signage_of_public_parking,
                                "location_of_public_parking_sports": location_of_public_parking_sports
                            },
                            "sidewalks": {
                                "availability_of_sidewalks": availability_of_sidewalks,
                                "usability_of_sidewalks": usability_of_sidewalks,
                                "condition_of_sidewalks": condition_of_sidewalks
                            }

                        },
                        "cleanliness_of_municipality": {
                            "cleanliness_city": cleanliness_city,
                            "cleanliness_municipality": cleanliness_municipality
                        },
                        "road_condition": {
                            "road_condition_city": road_condition_city,
                            "road_condition_municipality": road_condition_municipality,
                        },
                        "safety_at_night_with_the_street_lightning": Q11_A,
                        "satisfaction_with_social_services": {
                            "availability_of_parks_and_squares": Q11_B,
                            "usability_of_parks_and_squares": Q11_C,
                            "public_lightning_of_streets_and_public_spaces": Q11_D,
                            "environmental_protection": Q11_E,
                            "culture_youth_sport": {
                                "cultural_activities": Q11_F,
                                "youth_activities": Q11_G,
                                "sport_activities": Q11_H
                            },
                            "urban_and_rural_planning": {
                                "urban_and_rural_planning_functioning": Q11_I,
                                "implementation_of_building_regulations_and_control_standards": Q11_J,
                                "issuing_building_permits_as_positive": Q11_K
                            },

                            "social_and_family_welfare": {
                                "work_of_centre_for_social_welfare": Q12_A
                            },
                            "public_transport": {
                                "usage_of_public_transport": Q12_B,
                                "public_transport_services": Q12_C,
                                "time_it_takes_to_reach_their_destination": Q12_D
                            },
                        },
                        "Q13_A": Q13_A,
                        "Q13_B": Q13_B,
                        "Q13_C": Q13_C,
                        "Q13_D": Q13_D,
                        "Q13_E": Q13_E,
                        "Q13_F": Q13_F,
                        "Q13_G": Q13_G,
                        "Q13_H": Q13_H,
                        "Q13_I": Q13_I,
                        "Q13_J": Q13_J,
                        "Q14": Q14,
                        "Q15": Q15,
                        "Q15a": Q15a,
                        "Q16": Q16,
                        "Q17": Q17,
                        "Q18": Q18,
                    },
                    "Q19": Q19,
                    "Q20": Q20,
                    "Q21": Q21,
                    "Q22": Q22,
                    "Q23": Q23,
                    "Q24": Q24,
                    "Q25": Q25,
                    "Q26": Q26
                }
            }
            collection.insert(report)


parse()
