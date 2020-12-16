console.log ('it works')
var updateBtns = document.getElementsByClassName("update-cart")

for (i=0; i<updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)
        console.log('user:', user)
        if (user === 'AnonymousUser'){
            console.log('not logged in')
        }else{
            console.log('user is logged in, sending data ...')
        }
    })
}

