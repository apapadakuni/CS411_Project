#Insert data
db.alldata.insert({ username:'email',
	gender:'gender',
	weight_kg:'weight',
	height_cm:'height',
	age:'age',
	min_walk:'min_walk',
	cal_goal:'cal_goal',

	calendar:{
			Monday:{
				event1:{
					name:'event1_name',
					s_time:'event1_start',
					e_time:'event1_end',
					location:'location1'
				}
				event2:{
					name:'event2_name',
					s_time:'event2_start',
					e_time:'event2_end',
					location:'location2'
				}
				event3:{
					name:'event3_name',
					s_time:'event3_start',
					e_time:'event3_end',
					location:'location3'
				}
				event4:{
					name:'event4_name',
					s_time:'event4_start',
					e_time:'event4_end',
					location:'location4'
				}
			}

			Tuesday:{
				event1:{
					name:'event1_name',
					s_time:'event1_start',
					e_time:'event1_end',
					location:'location1'
				}
				event2:{
					name:'event2_name',
					s_time:'event2_start',
					e_time:'event2_end',
					location:'location2'
				}
				event3:{
					name:'event3_name',
					s_time:'event3_start',
					e_time:'event3_end',
					location:'location3'
				}
				event4:{
					name:'event4_name',
					s_time:'event4_start',
					e_time:'event4_end',
					location:'location4'
				}
			}

			Wednesday:{
				event1:{
					name:'event1_name',
					s_time:'event1_start',
					e_time:'event1_end',
					location:'location1'
				}
				event2:{
					name:'event2_name',
					s_time:'event2_start',
					e_time:'event2_end',
					location:'location2'
				}
				event3:{
					name:'event3_name',
					s_time:'event3_start',
					e_time:'event3_end',
					location:'location3'
				}
				event4:{
					name:'event4_name',
					s_time:'event4_start',
					e_time:'event4_end',
					location:'location4'
				}
			}

			Thursday:{
				event1:{
					name:'event1_name',
					s_time:'event1_start',
					e_time:'event1_end',
					location:'location1'
				}
				event2:{
					name:'event2_name',
					s_time:'event2_start',
					e_time:'event2_end',
					location:'location2'
				}
				event3:{
					name:'event3_name',
					s_time:'event3_start',
					e_time:'event3_end',
					location:'location3'
				}
				event4:{
					name:'event4_name',
					s_time:'event4_start',
					e_time:'event4_end',
					location:'location4'
				}
			}

			Friday:{
				event1:{
					name:'event1_name',
					s_time:'event1_start',
					e_time:'event1_end',
					location:'location1'
				}
				event2:{
					name:'event2_name',
					s_time:'event2_start',
					e_time:'event2_end',
					location:'location2'
				}
				event3:{
					name:'event3_name',
					s_time:'event3_start',
					e_time:'event3_end',
					location:'location3'
				}
				event4:{
					name:'event4_name',
					s_time:'event4_start',
					e_time:'event4_end',
					location:'location4'
				}
			}

			Saturday:{
				event1:{
					name:'event1_name',
					s_time:'event1_start',
					e_time:'event1_end',
					location:'location1'
				}
				event2:{
					name:'event2_name',
					s_time:'event2_start',
					e_time:'event2_end',
					location:'location2'
				}
				event3:{
					name:'event3_name',
					s_time:'event3_start',
					e_time:'event3_end',
					location:'location3'
				}
				event4:{
					name:'event4_name',
					s_time:'event4_start',
					e_time:'event4_end',
					location:'location4'
				}
			}

			Sunday:{
				event1:{
					name:'event1_name',
					s_time:'event1_start',
					e_time:'event1_end',
					location:'location1'
				}
				event2:{
					name:'event2_name',
					s_time:'event2_start',
					e_time:'event2_end',
					location:'location2'
				}
				event3:{
					name:'event3_name',
					s_time:'event3_start',
					e_time:'event3_end',
					location:'location3'
				}
				event4:{
					name:'event4_name',
					s_time:'event4_start',
					e_time:'event4_end',
					location:'location4'
				}
			}
},

		suggest_calendar:{

			Monday:{
				event1:{
				s_time:'event1_end',
				e_time:'event2_start',
				duration:'duration',
				method:'method',
				calories:'calories'
				}

				event2:{
				s_time:'event2_end',
				e_time:'event3_start',
				duration:'duration',
				method:'method',
				calories:'calories'
				}

				event3:{
				s_time:'event3_end',
				e_time:'event4_start',
				duration:'duration',
				method:'method',
				calories:'calories'
				}
			}

			Tuesday:{
				event1:{
				s_time:'event1_end',
				e_time:'event2_start',
				duration:'duration',
				method:'method',
				calories:'calories'
				}

				event2:{
				s_time:'event2_end',
				e_time:'event3_start',
				duration:'duration',
				method:'method',
				calories:'calories'
				}

				event3:{
				s_time:'event3_end',
				e_time:'event4_start',
				duration:'duration',
				method:'method',
				calories:'calories'
				}
			}

			Wednesday:{
				event1:{
				s_time:'event1_end',
				e_time:'event2_start',
				duration:'duration',
				method:'method',
				calories:'calories'
				}

				event2:{
				s_time:'event2_end',
				e_time:'event3_start',
				duration:'duration',
				method:'method',
				calories:'calories'
				}

				event3:{
				s_time:'event3_end',
				e_time:'event4_start',
				duration:'duration',
				method:'method',
				calories:'calories'
				}
			}

			Thursday:{
				event1:{
				s_time:'event1_end',
				e_time:'event2_start',
				duration:'duration',
				method:'method',
				calories:'calories'
				}

				event2:{
				s_time:'event2_end',
				e_time:'event3_start',
				duration:'duration',
				method:'method',
				calories:'calories'
				}

				event3:{
				s_time:'event3_end',
				e_time:'event4_start',
				duration:'duration',
				method:'method',
				calories:'calories'
				}
			}

			Friday:{
				event1:{
				s_time:'event1_end',
				e_time:'event2_start',
				duration:'duration',
				method:'method',
				calories:'calories'
				}

				event2:{
				s_time:'event2_end',
				e_time:'event3_start',
				duration:'duration',
				method:'method',
				calories:'calories'
				}

				event3:{
				s_time:'event3_end',
				e_time:'event4_start',
				duration:'duration',
				method:'method',
				calories:'calories'
				}
			}

			Saturday:{
				event1:{
				s_time:'event1_end',
				e_time:'event2_start',
				duration:'duration',
				method:'method',
				calories:'calories'
				}

				event2:{
				s_time:'event2_end',
				e_time:'event3_start',
				duration:'duration',
				method:'method',
				calories:'calories'
				}

				event3:{
				s_time:'event3_end',
				e_time:'event4_start',
				duration:'duration',
				method:'method',
				calories:'calories'
				}
			}

			Sunday:{
				event1:{
				s_time:'event1_end',
				e_time:'event2_start',
				duration:'duration',
				method:'method',
				calories:'calories'
				}

				event2:{
				s_time:'event2_end',
				e_time:'event3_start',
				duration:'duration',
				method:'method',
				calories:'calories'
				}

				event3:{
				s_time:'event3_end',
				e_time:'event4_start',
				duration:'duration',
				method:'method',
				calories:'calories'
				}
			}
		}
	})

#Read username by its email address 
u_name = db.alldata.find({"username":"email"}).pretty();

#Update profile
db.alldata.update({'username':'email'},{$set:{'username':'newemail'}})

def getallinfo(email):
 allinfo=db.collection.find({username:/email/})   #collection is the variable stores collection name
 return allinfo
def getPersonalinfo(email):
 personalinfo=db.collection.find({username:/email/},{personalinfo:1})
 return personalinfo
def getCalendar(email)：
 calendar=db.collection.find({username:/email/},{calendar:1})
  return calendar
 def getSuggestcalendar(email):
 suggestcalendar=db.collection.find({username:/email/},{suggest_calendar:1})
#     return suggestcalendar