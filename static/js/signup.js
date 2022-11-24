(function () {
  'use strict'

  // Get all the forms we want to apply custom Bootstrap validation styles
  var forms = document.querySelectorAll('.needs-validation')

  // Fixate on them and prevent sending
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
})()
