# Plexhacks 2020  - UCBerkeleyHackathon

• Project name: Social Justice During the COVID-19 Pandemic


[![Youtube Video Demonstration(https://www.youtube.com/watch?v=XkdEMrCjJpE&feature=youtu.be
 "Hackathon Video")


• Description: During the COVID-19 pandemic, we are all concerned about public health and safety, but social justice is crucial and should not be forgotten. From the past up till now, people in the United States have been treated unequally. With these two situations in mind, this project prepares the data from the Twitter social media site using hashtags and user locations to trace where demonstrations occur as well as the data from the Kaggle website (primary source: The New York Times) to check which location has a high number of corona virus cases. You can make API requests and create data visualizations by using these datasets.
	
•Installation: No need to install, what you need to do is to apply for a developer account in Twitter (https://developer.twitter.com/en/docs...). If you want, you can install JupyterLab in your local computer. Alternatively, you can run JupyterLab online.  https://hub.gke.mybinder.org/user/jupyterlab-jupyterlab-demo-2d0hqm4r/lab  


•	Usage: Importing all necessary libraries

```ruby
	import http.client 
	import mimetypes
	import json
	import matplotlib.pyplot as plt
	import numpy as np
	from wordcloud import WordCloud, STOPWORDS 
	import matplotlib.pyplot as plt 
	import pandas as pd 
	import mimetypes

```

HTTP GET request to connect to the Twitter API and get response data in JSON format. Replace #add bearer key with your bearer token and # add personalization to your personalization id


```ruby
conn = http.client.HTTPSConnection("api.twitter.com")
payload = ''
headers = {
  'Authorization': 'Bearer', #add bearer key
  'Cookie': 'personalization_id="'# add personalization
}
conn.request("GET", "/1.1/search/tweets.json?q=BlackLivesMatter%20since:2020-05-20&lang=en&%23protestl&result_type=recent", payload, headers)
res = conn.getresponse()
data = res.read()
#print(data.decode("utf-8"))

unstructured_tweets = json.loads(data)
indent_tweets = json.dumps(json.loads(data), indent=2)
#print(indent_tweets)
#print(unstructured_tweets)
data = json.loads(indent_tweets)

with open('tweets.json', 'w') as f:
    json.dump(data, f, indent=4)

text = ''
with open("game.txt", "w", encoding='utf-8') as text_file:
    for status in data['statuses']:
        text += status['text']
        text += ' '
        print(status['text'])
        text_file.write(status['text'])
```


Sample output from the code above

```ruby
We are living in 21st century and there is racism in the world which  caused the protest for black rights with… https://t.co/y6CclKtATO
RT @Lady44Sassy: #BlackLivesMatter are nothing but scum ..Always attack in packs, to cowardly for one on one... Look at them all surroundin…
#BlackLivesMatter protests showed that people all over the world are tired of racism and discrimination. They want… https://t.co/mnA8oiOqAx
RT @BKCASHMERE: "What's Going On Now" Out Now 🔥🔥🔥 #linkinbio https://t.co/N2dMYqtjbX Subscribe to the Channel!!! #Newvideo #film #videogame…
Today a white dude that I see at work and generally enjoy talking to said to me: “I don’t agree with any of that sh… https://t.co/A0tJWqwpbV
RT @MarxistKittyCat: If you follow me, I will follow you back as soon as Twitter let's me! 

🐢Slowly 🐢 but 🐢 surely 🐢

@MarxistKittyCat

#N…
RT @kenmagukkie: since blm is slowly fading away from my tl and my other social media’s, here’s a thread+petitions you can sign #BlackLives…
RT @SJDKennington: Thanks guys ⁦@UTCAI_⁩ for your leadership and inspiration. You bring hope that things can change if we work together #Bl…
RT @btsloonapop: hallyu will eventually fall off if koreans do not educate themselves on other cultures #나는_샘_오취리와_연대합니다
#I_Stand_with_Sam_…
RT @sailorrooscout: Psst.

#BlackLivesMatter is always relevant. It’s not going away. Get used to it. 

KEEP PROTESTING. 
KEEP SIGNING PETI…
#BlackLivesMatter protests showed that people all over the world are tired of racism and discrimination. They want… https://t.co/DVMfZHYwoD
We are living in 21st century and there is racism in the world which  caused the protest for black rights with… https://t.co/WN31HNpBXG
RT @ColorOfChange: CEOs in ivory towers “support” of #BlackLivesMatter means nothing when they don’t use the funds at their disposal to mak…
RT @CrunchyConserv3: We lost an officer this week, he was retired navy, a 20+ year officer, a youth football coach, a husband &amp; father. Sup…
The Proud Boys are apart of the @MLB now? Disgusting, @Athletics! His lame excuse will not work! Ryan Christenson i… https://t.co/l7KyCB4GG1
```
We will get rid of bad characters - this part can be customized to your preference.

```ruby
	comment_words = ''
	stopwords = set(STOPWORDS)
	bad_chars = [';', ':', '!', "*"] 
	for val in text.split(' '):
	    val = str(val)
	    for i in bad_chars : 
	        val = val.replace(i, '')
	    tokens = val.split()
	    for i in range(len(tokens)):
	        tokens[i] = tokens[i].lower()
	    if len(val)> 4:
	        comment_words += " ".join(tokens) + " "
	wordcloud = WordCloud().generate(comment_words)
	print(comment_words)

```
We get this output after running the above code. 

```ruby
living century there racism world which caused protest black rights with… https//t.co/y6cclktato @lady44sassy #blacklivesmatter nothing ..always attack packs, cowardly one... surroundin… #blacklivesmatter protests showed people world tired racism discrimination. want… https//t.co/mna8oioqax @bkcashmere "what's going #linkinbio https//t.co/n2dmyqtjbx subscribe channel #newvideo #film #videogame… today white generally enjoy talking don’t agree https//t.co/a0tjwqwpbv @marxistkittycat follow follow twitter let's 🐢slowly surely 🐢 @marxistkittycat #n… @kenmagukkie since slowly fading other social media’s, here’s thread+petitions #blacklives… @sjdkennington thanks ⁦@utcai_⁩ leadership inspiration. bring things change together @btsloonapop hallyu eventually koreans educate themselves other cultures #나는_샘_오취리와_연대합니다 #i_stand_with_sam_… @sailorrooscout psst. #blacklivesmatter always relevant. going away. keep protesting. keep signing peti… #blacklivesmatter protests showed people world tired racism discrimination. want… https//t.co/dvmfzhywod living century there racism world which caused protest black rights with… https//t.co/wn31hnpbxg @colorofchange ivory towers “support” #blacklivesmatter means nothing don’t funds their disposal @crunchyconserv3 officer week, retired navy, officer, youth football coach, husband father. proud apart disgusting, @athletics excuse christenson https//t.co/l7kycb4gg1 
```

After mining the data from the Twitter API, you can use the obtained data in your project. In this example, we make a Word Cloud depicting the sentiments of the general populace on Twitter regarding the Black Lives Matter movement. 

```ruby
	wordcloud = WordCloud(width = 800, height = 800, 
        	background_color ='white', 
		stopwords = stopwords, 
		min_font_size = 10).generate(comment_words) 
	plt.figure(figsize = (8, 8), facecolor = None) 
	plt.imshow(wordcloud) 
	plt.axis("off") 
        plt.tight_layout(pad = 0) 

	plt.show()

```

We use another dataset to analyze COVID-19 cases. We import all the libraries we need and obtain the live dataset from Kaggle.com (primary source: New York Times). Select a portion of the data you want to work with - in this case we want data from three days back from the present date.

```ruby
import numpy as np
import pandas as pd
import seaborn as sns
import plotly
import matplotlib as plt
import plotly.graph_objects as go
import plotly.express as px
import plotly.offline as pyo
from datetime import date, timedelta
import folium
from scipy.interpolate import interp1d
pyo.init_notebook_mode()

covid = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv", error_bad_lines = False)

today = date.today()
three_days_back = (today - timedelta(days=3)).strftime('%Y-%m-%d')
covid_latest = covid[covid.date.eq(three_days_back)]
covid_states_lst = np.array([ 'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Guam', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Northern Mariana Islands', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virgin Islands', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']) 
covid_state_total = covid_latest.groupby('state', as_index = False).sum()
print(covid_state_total)

```

We will get data of COVID-19 cases in each state in the US

```ruby
                       state   cases  deaths
0                    Alabama   94654    1695
1                     Alaska    4181      23
2                    Arizona  182230    3933
3                   Arkansas   46293     508
4                 California  532776    9866
5                   Colorado   49143    1857
6                Connecticut   50225    4437
7                   Delaware   15296     587
8       District of Columbia   12443     587
9                    Florida  502731    7626
10                   Georgia  186395    3899
11                      Guam    1358       6
12                    Hawaii    2740      26
13                     Idaho   22854     218
14                  Illinois  188474    7776
15                   Indiana   71685    3007
16                      Iowa   46836     900
17                    Kansas   30047     371
18                  Kentucky   33823     771
19                 Louisiana  126061    4096
20                     Maine    3992     124
21                  Maryland   93000    3536
22             Massachusetts  119643    8659
23                  Michigan   94045    6480
24                 Minnesota   57820    1670
25               Mississippi   63444    1804
26                  Missouri   55919    1337
27                   Montana    4481      65
28                  Nebraska   27497     342
29                    Nevada   52919     891
30             New Hampshire    6719     418
31                New Jersey  185180   15842
32                New Mexico   21566     667
33                  New York  422935   32431
34            North Carolina  129511    2079
35              North Dakota    7061     112
36  Northern Mariana Islands      46       2
37                      Ohio   96305    3596
38                  Oklahoma   40555     583
39                    Oregon   19979     342
40              Pennsylvania  120492    7310
41               Puerto Rico   19651       0
42              Rhode Island   19481    1012
43            South Carolina   95472    1894
44              South Dakota    9168     137
45                 Tennessee  111305    1130
46                     Texas  480789    8149
47                      Utah   42478     330
48                   Vermont    1436      57
49            Virgin Islands     501       9
50                  Virginia   95049    2274
51                Washington   62390    1705
52             West Virginia    7159     124
53                 Wisconsin   61247     979
54                   Wyoming    2923      27

```
Now we are going to make a data visualization and we will use it for the application 

```ruby
fig = go.Figure(data=[
go.Bar(name='Cases', x=covid_state_total['state'], y= covid_state_total['cases']),
go.Bar(name='Deaths', x=covid_state_total['state'], y= covid_state_total['deaths'])
]
)
fig.update_layout(title="COVID-19 Cases in the United States as of " + three_days_back, barmode='group')
fig.show()

```

// picture of the output
```ruby
fig = px.sunburst(covid_latest, path=['state','county'], values = 'cases')
fig.update_layout(title = "COVID-19 Cases by State, County as of " + three_days_back)
fig.show()

```
// picture of the output

For the visualizations, please refer to COVID-19.ipynb (https://github.com/18Badenm/UCBerkleyHackathon/blob/master/COVID-19.ipynb)!

This is an example of the implementation done from the **New York Times** 'live' COVID-19 dataset

<video width="320" height="240" controls>
  <source src="Example inplemetation.mp4" type="video/mp4">
</video>
