import re
import os

def regex_renamer():

	# Taking input from the user

	print("1. Breaking Bad")
	print("2. Game of Thrones")
	print("3. Lucifer")

	webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))   
	season_padding = int(input("Enter the Season Number Padding: "))
	episode_padding = int(input("Enter the Episode Number Padding: "))

	series = {1 : "Breaking Bad", 2 : "Game of Thrones", 3 : "Lucifer"}					#mapping series according to webseries_num

	start = [0, 1000, 4, 2]																#Episode name starts from this index
	end = [0, -1000, 5, 4]																#Episode name ends from this index
	pat = [0, 2, 3, 1]																	#name of webseries ends here in file name

	path = "wrong_srt/" + series[webseries_num]											#path of given series
	for episode in os.listdir(path) :													#iterating all files in folder of webseries
		old_path = path + '/' + episode													#path of the file
		words = re.compile(r'\w+')														#using regex
		words_found = re.findall(words, episode)										#words found in the name of file
		num = re.compile(r'\d+')														#using regex
		num_found = re.findall(num, episode)											#numbers found in the name of file
		season_num =  str(int(num_found[0]))											#finding season number
		episode_num = str(int(num_found[1]))											#finding episode number
		cnt = -1																		#counter
		episode_name = ""
		new_path = ""
		for x in words_found :
			cnt += 1
			if cnt < pat[webseries_num] :												#making new path
				new_path += x + " "
			if cnt < start[webseries_num] :
				continue
			if cnt >= len(words_found) - end[webseries_num] :
				continue
			episode_name += x															#finding episode name
			if cnt < len(words_found) - end[webseries_num] - 1 :
				episode_name += ' '
		new_s = ""																		#season number with padding
		new_e = ""																		#episode number with padding
		cnt = season_padding - len(season_num)
		for x in range(cnt) :
			new_s += '0'																#padding
		cnt = episode_padding - len(episode_num)
		for x in range(cnt) :
			new_e += '0'																#padding
		new_s += season_num
		new_e += episode_num
		new_path += "Season " + new_s + " " + "Episode " + new_e						#making new_path
		if webseries_num >= 2 :
			new_path += " " + episode_name
		new_path += "." + words_found[-1]												#making new_path
		new_path = path + "/" + new_path												#making new_path
		os.rename(old_path, new_path)													#renaming file as per requirement



regex_renamer()