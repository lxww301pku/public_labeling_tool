var wwtag = 'title';

(function () {
    function contentLoaded () {    
            window.addEventListener('keypress', function (e) {
            if (e.keyCode === 115) {
                window.wwtag = 'source';
            }
            else if (e.keyCode === 116){
                window.wwtag = 'tv';
            }
            else{
                window.wwtag = 'title';
            }
            }, false);
    }
    window.addEventListener('DOMContentLoaded', contentLoaded, false); 
}());

function getSelText()
{
    var txt = '';
     if (window.getSelection)
    {
        txt = window.getSelection();
     }
    else if (document.getSelection)
    {
        txt = document.getSelection();
    }
    else if (document.selection)
    {
        txt = document.selection.createRange().text;
    }
    return txt;
}

function getKeyboard(event)
{
    return event.which || event.keyCode;
}

function sendString(buttonId, event)
{
    //document.getElementsByName(buttonId)[0].value += 'title'+ '=' + getSelText() + '\t';
    $('textarea[name='+buttonId+']')[0].value += wwtag + '=' + getSelText() + '\t';
}
