$(document).ready(function(){
// to show the login form when the button is clicked
    $(".btn").click(function(){
       //function to handle the event
        $("#formhideshow").show();
    });
    $( function() {
        $( "#datepicker" ).datepicker();
      } );
});
// form validation

/*
create the function of name validation
get the inputs form the form and store them in variables
validate if the user has given the input are not
validate for proper data
*/
function formvalidation(){
    var name=document.getElementById("name");
    var email=document.getElementById("email");
    var number=document.getElementById("number");
    var address= document.getElementById("address");
    var landmark = document.getElementById("landmark")
    var message=" is not correct";
    //   store validation expresions
        var emailExp = /^([a-zA-z0-9\.-]+)([@])([a-zA-z0-9-]+.)([a-z]{2,8})(.[a-z]{2,8})?$/;
        var telExp = /^([0-9]{10})$/;
        var textOnlyExp = /^([a-zA-Z]+)$/;
    // check whether the text are are correct are not 
    if(name.nodeValue>6 && name.nodeValue<15){
        return true;
    }else if(number.value>=10){
        return true;
    }else if(address.value>30){
        return true;
    }else if(landmark.value>30){
        return true;
    }else{
        document.write("Your details are not correct")
    }
}