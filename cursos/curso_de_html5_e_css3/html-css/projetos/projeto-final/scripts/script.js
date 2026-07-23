const darkmode_button = document.getElementById('darkmode-button');
const darkmode_button_icon = document.querySelector('#darkmode-button span');
const body = document.body;

let tema = localStorage.getItem('tema') || 'light';
aplicarTema(tema)

darkmode_button.addEventListener('click', () => {
  tema = (tema === 'light') ? 'dark' : 'light';
  localStorage.setItem('tema', tema);
  aplicarTema(tema)
})

function aplicarTema(tipo) {
  if (tipo === 'light') {
    body.classList.remove('dark')
    darkmode_button_icon.innerHTML = '<i class="fa-solid fa-moon"></i>'
  } else if (tipo === 'dark') {
    body.classList.add('dark')
    darkmode_button_icon.innerHTML = '<i class="fa-solid fa-sun"></i>'
  }
}