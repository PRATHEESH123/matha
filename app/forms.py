from django import forms
from .models import contact_tble

class contact_tbleForm(forms.ModelForm):
    model = contact_tble
    fields ='__all__'

    # <!-- {% for i in data %}
    #     <tr>
    #         <td>{{i.id}}</td>
    #         <td>{{i.tittle}}</td>
    #         <td><img src="{{i.img}}" alt="" height="" width="320"></td>
    #         <td>{{i.discription}}</td>
    #         <td>{{i.link}}</td>
    #         <li><a href="{% url 'aboutedit' %}">EDIT</a></li>
    #         <td><a href="{% url 'aboutdelete' id=i.id %}">DELETE</a></td>
    #         <td><img src="{{i.img}}" height="50" width="50"></td>
    #         </tr>
    # {% endfor %} -->