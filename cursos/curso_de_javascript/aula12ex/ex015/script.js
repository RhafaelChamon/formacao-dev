window.document.querySelector('#botao').addEventListener('click', clicar)

function clicar() {
    var anoatual = new Date().getFullYear()
    var nasc = document.querySelector('#ano_nasc').value
    var op_sexo = document.getElementsByName('sex')
    var resu = window.document.querySelector('#res')
    var img = document.createElement('img')
    
    if (nasc.length == 0 || nasc > anoatual) {
        alert('[ERRO] Verifique os dados novamente.')
    } else {
        var idade = anoatual - Number(nasc)
        
        if (op_sexo[0].checked) {
            var sexo = 'um homem'
        } else {
            var sexo = 'uma mulher'
        }
        
        if (sexo == 'um homem') {
            if (idade < 12) {
                img.src = 'fotos/foto-bebe-m.png'
            } else if (idade < 18) {
                img.src = 'fotos/foto-adolescente-m.png'
            } else if (idade < 30) {
                img.src = 'fotos/foto-jovem-m.png'
            } else if (idade < 60) {
                img.src = 'fotos/foto-adulto-m.png'
            } else {
                img.src = 'fotos/foto-idoso-m.png'
            }
        } else {
            if (idade < 12) {
                img.src = 'fotos/foto-bebe-f.png'
            } else if (idade < 18) {
                img.src = 'fotos/foto-adolescente-f.png'
            } else if (idade < 30) {
                img.src = 'fotos/foto-jovem-f.png'
            } else if (idade < 60) {
                img.src = 'fotos/foto-adulto-f.png'
            } else {
                img.src = 'fotos/foto-idoso-f.png'
            }
        }

        resu.innerHTML = `<p>Foi identificado ${sexo} com ${idade} anos.</p>`
        resu.appendChild(img)
    } 
}