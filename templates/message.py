{% load static %}
<link href="{% static 'assets/css/scrollspyNav.css' %}" rel="stylesheet" type="text/css" />
    <link href="{% static 'plugins/animate/animate.css' %}" rel="stylesheet" type="text/css" />
    <script src="{% static 'plugins/sweetalerts/promise-polyfill.js' %}"></script>
    <link href="{% static 'plugins/sweetalerts/sweetalert2.min.css' %}" rel="stylesheet" type="text/css" />
    <link href="{% static 'plugins/sweetalerts/sweetalert.css' %}" rel="stylesheet" type="text/css" />
    <link href="{% static 'assets/css/components/custom-sweetalert.css' %}" rel="stylesheet" type="text/css" />



    {% if messages %}

    {% for message in messages %}
    <script>

        window.onload = (function() {
        swal({
            title: '{{message}}',
            type: '{{message.tags}}',
            timer: 2000,
            padding: '2em',
            onOpen: function () {
            swal.showLoading()
            }
        }).then(function (result) {
            if (
            // Read more about handling dismissals
            result.dismiss === swal.DismissReason.timer
            ) {
            console.log('I was closed by the timer')
            }
        })
        })

    </script>
    {% endfor %}

    {% endif %}


    <!-- {% if messages %}
<div class="messages">
    {% for message in messages %}

    <script>
      window.onload = (function() {
    
        Swal.fire({
            icon: "{{message.tags}}",
            title: "{{message}}",
            showConfirmButton: false,
            timer: 2500
          });
      });
    </script>

    {% endfor %}
</div>
{% endif %} -->
                                        



    <script src="{% static 'assets/js/scrollspyNav.js' %}"></script>
    <script src="{% static 'plugins/sweetalerts/sweetalert2.min.js' %}"></script>
    <script src="{% static 'plugins/sweetalerts/custom-sweetalert.js' %}"></script>