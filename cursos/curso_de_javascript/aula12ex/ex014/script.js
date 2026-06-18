var hora = new Date().getHours()
var msg = window.document.querySelector('#msg p')
var foto = window.document.querySelector('#foto img')
var cor_fundo = window.document.body.style

msg.textContent = `Agora são ${hora} horas`
if (hora < 6) {
    foto.src = 'fotos/fotomadrugada.png'
    cor_fundo.background = '#061b21'
} else if (hora < 12) {
    foto.src = 'fotos/fotomanha.png'
    cor_fundo.background = '#aea899'
} else if (hora < 18) {
    foto.src = 'fotos/fototarde.png'
    cor_fundo.background = '#f79a1c'
} else {
    foto.src = 'fotos/fotonoite.png'
    cor_fundo.background = '#1b284c'
}
