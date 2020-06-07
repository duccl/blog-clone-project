const get_content = () => {
    $("#content").html($("#content").text())
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