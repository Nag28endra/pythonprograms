fav_lang ={
             'vamsi':'python',
             'shashank':'java',
              'venkatesh':'html',
              'manoj':'java',
              'harshath':'python',
              'namratha':'java',
              'preeti':'python',
              'keerthi':'c++',
              'likitha':'java',
              'vyshali':'python',
              'madhuri':'c',
              'sruthi':'python',
            }
languages= {}
for lang in fav_lang.values():
    languages.setdefault(lang,0)
    languages[lang] +=1

print(languages)
