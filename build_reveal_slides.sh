jupyter-nbconvert --to slides slides.ipynb --reveal-prefix=reveal.js
mv slides.slides.html index.html
sed -i 's#<title>slides slides</title>#<title>Transit Data and OpenStreetMap</title>#g' \
  index.html
