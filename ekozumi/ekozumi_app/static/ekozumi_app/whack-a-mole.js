/** Whack a mole fight script
 * 
 *  Author: Jacob Beeson
 */

const cursor = document.querySelector('.cursor')
const holes = [...document.querySelectorAll('.holes')]

const health1 = document.querySelector('.health span')
let health = 100

const whack = new Audio("../../static/Sounds/whack.mp3")
const music = new Audio("../../static/Sounds/background-tune.mp3")

var seconds = 60;

// displayes countdown/checks if time is up
function startTimer() {
  var countdown = setInterval(function() {
    seconds--;
    document.getElementById("seconds").textContent = pad(seconds);
    if (seconds == 0) {
      //game lost
      clearInterval(countdown);
      alert("LOST GAME, Click 'ok' to return home");
      window.location = "../home"
    }
  }, 1000);
}

// adds a '0' to single digits ('2' -> '02')
function pad(num) {
  return ("0" + num).slice(-2);
}

//game code
function run(){
    //gets the index of a random hole 
    const i = Math.floor(Math.random() * holes.length)
    const hole = holes[i]
    const img = document.createElement('img')
    //adds the image of 'mole' to the hole
    img.classList.add('mole')
    img.src = moleImage
    
  //when player hits the 'mole'
    img.addEventListener('click', () => {
        health -= 10
        whack.play()
        img.src = whackedMoleImage
        health1.textContent = health
        if(health!=0){
            clearTimeout(timer)
            setTimeout(() => {
                hole.removeChild(img)
                run()
            }, 500)
        }else{
            //game won
            hole.removeChild(img)
            alert("YOU HAVE DEFEATED THE BOSS! Click 'ok' to progress");
            window.location = "../fight_outro";
        }
    })
    // adds 'mole' to hole
    hole.appendChild(img)

    timer = setTimeout(() => {
        hole.removeChild(img)
        run()
      //time that the 'mole' stays in the hole
    }, 800)
}

window.addEventListener('mousemove', e =>{
    cursor.style.top = e.pageY + 'px'
    cursor.style.left = e.pageX + 'px'
})

//animates the hammer moving on click
window.addEventListener('mousedown', () => {
    cursor.classList.add('active')
})

window.addEventListener('mouseup', () => {
    cursor.classList.remove('active')
})  

function startGame(i1,i2){
    moleImage = i1
    whackedMoleImage = i2
    music.volume = 0.2;
    music.play()
    var elem = document.getElementById("startButton");
    elem.parentNode.removeChild(elem);
    startTimer()
    run();
}
