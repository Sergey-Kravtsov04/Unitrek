let button = $('input[type="submit"]')
button.mouseover(function (e){button.css('color','red')})
button.mouseout(function (e){button.css('color','black')})
let inputs = [$('input[type="text"]'),$('input[type="email"]'),$('textarea')]
console.log(inputs)
for(let element of inputs){
    element.on('focus',function (e){element.css('background-color','#FFAA00')})
    element.on('blur',function (e){element.css('background-color','#FFBF40')})
}