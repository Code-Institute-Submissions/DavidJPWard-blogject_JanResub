var myModal = document.getElementById('exampleModal')
var myInput = document.getElementById('delete-button')

myModal.addEventListener('shown.bs.modal', function () {
  myInput.focus()
  console.log("done")
})
