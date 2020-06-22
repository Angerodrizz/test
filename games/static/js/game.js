document.addEventListener('DOMContentLoaded', () => {


    let getRandomNumber = size => {
        return Math.floor(Math.random() * size);
    }

    let getDistance = (e, target) => {
        let diffX = e.offsetX - target.x;
        let diffY = e.offsetY - target.y;
        return Math.sqrt((diffX * diffX) + (diffY + diffY));
    }

    let getDistanceHint = distance => {
        if (distance < 30) {
            return "Really Close";
        }
        else if (distance < 40) {
            return "Close";
        }
        else if (distance < 60) {
            return "A bit close";
        }
        else if (distance < 100) {
            return "Not too close";
        }
        else if (distance < 180) {
            return "A bit far away";
        }
        else if (distance < 360) {
            return "Far, far away";
        }
        else {
            return "Freezing, Keep Trying";
        }
    }

    const WIDTH = 500;
    const HEIGHT = 500;

    let target = {
        x: getRandomNumber(WIDTH),
        y: getRandomNumber(HEIGHT)
    };

    let $map = document.querySelector('#map');   
    let $distance = document.querySelector('#distance');
    let clicks = 0;


    $map.addEventListener('click', function (e) {
        console.log('click');
        clicks++;
        let distance = getDistance(e, target);
        let distanceHint = getDistanceHint(distance);
        $distance.innerHTML = `<h1>${distanceHint}</h1>`;
    
        if (distance < 20 ) {
        alert(`Found the treasure in ${clicks} clicks!`);
        location.reload();
        }
    });

});