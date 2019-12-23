a = [2, 1, 4, 5, 3, 7, 8]

def sort(li):
    n = len(li)
    print(n)
    for i in range(1, n):

        while i > 0 and li[i - 1] > li[i]:
            li[i], li[i - 1] = li[i - 1], li[i]
            i-=1

    print(li)



def sort2(li):
    n = len(li)
    print(n)
    for i in range(1, n):

        while i > 0 and li[i - 1] > li[i]:
            li[i], li[i - 1] = li[i - 1], li[i]
            i-=1

    print(li)

b = [2, 1, 4, 5, 3, 7, 8]

c = [2, 1, 4, 5, 3, 7, 8]
sort(a)


# mkdir project
# cd project
# python -m venv venv
#
# venv\Scripts\activate.bat





{#      {% for post in news %}#}
{#          {%  if news.index %}#}
{#          <div class="row featurette mt-5">#}
{#          <div class="col-md-7">#}
{#              <h2 class="featurette-heading">{{ post.title }} </h2>#}
{#              <p class="lead">{{ post.text| striptags|truncatechars:200 }}</p>#}
{#          </div>#}
{#          <div class="col-md-5 ">#}
{#              <img class="d-block w-100" src="{{ post.img|safe }}">#}
{#          </div>#}
{##}
{#          <a href="{% url 'full_news' post.id %}" class="btn btn-outline-secondary">Читать далее</a>#}
{#          <hr class="featurette-divider">#}
{##}
{#          {% endif %}#}
{#      {% endfor %}#}

