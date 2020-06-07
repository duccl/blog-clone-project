const get_content = () => {
    $(".text-break").each(function(){
        $(this).html($(this).text())
    }) 
}

const textareaPresent = () =>{
    return $('textarea').length == 1;
}

window.onload = () => {
    if(textareaPresent()){
        let textAreaName = $('textarea').attr('name')
        CKEDITOR.replace(textAreaName);
    }
}

get_content()