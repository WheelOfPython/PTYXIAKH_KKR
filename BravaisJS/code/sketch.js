let AtomsNumber = 4;
let AtomsColors = ['red', 'yellow', 'yellow', 'green','blue', 'yellow', 'purple'];

let AtomsInputs = [];
let PointsInputs = [];
let Vecs = [];
let Atoms = [];

let _width  = 600;
let _height = 400;

let posX = _width / 4;
let posY = _height / 4;

let angle = 0; //RADIANS!! --> 0 == 6.28
let dist = 3;
let line_size  = 0.1;
let ISO = false;

let points = [];
let pointsAtoms = [];



function makeCrystal(_a, _b, _c, rows, cols, zett, points, Atoms){
  dist = 2*findMax(Atoms) + 1;
  makeGrid(_a, _b, _c, rows, cols, zett, points);
  putAtoms(Atoms, _a, _b, _c, rows, cols, zett, pointsAtoms);
}

let FCC = [[[1, 0, 0], [0,1,0], [0,0,1]], [[0,0,0], [0.5, 0.5, 0], [0.5, 0,0.5], [0,0.5,0.5]]];
//if sel.selected()
function makeFCC(){
  for (let vec=0; vec < 3; vec++){
    Vecs[vec] = createVector(
    PointsInputs[vec][0].value(FCC[0][vec][0]), 
    PointsInputs[vec][1].value(FCC[0][vec][1]), 
    PointsInputs[vec][2].value(FCC[0][vec][2])
    );
  }

  for (let atom=0; atom < AtomsNumber; atom++){
  Atoms[atom] = createVector(
    AtomsInputs[atom][0].value(FCC[1][atom][0]), 
    AtomsInputs[atom][1].value(FCC[1][atom][1]), 
    AtomsInputs[atom][2].value(FCC[1][atom][2])
    );
  }
  greet();
}


function greet(){
for (let vec=0; vec < 3; vec++){
  Vecs[vec] = createVector(
    parseFloat(PointsInputs[vec][0].value()), 
    parseFloat(PointsInputs[vec][1].value()), 
    parseFloat(PointsInputs[vec][2].value()));
}

for (let atom=0; atom < AtomsNumber; atom++){
  Atoms[atom] = createVector(
    parseFloat(AtomsInputs[atom][0].value()), 
    parseFloat(AtomsInputs[atom][1].value()), 
    parseFloat(AtomsInputs[atom][2].value()));
}

points = [];
pointsAtoms = [];
makeCrystal(Vecs[0], Vecs[1], Vecs[2], rows, cols, zett, points, Atoms)
}

///////////////////////////////////////////////////////////////////////
////////////////////////////// MAIN CODE //////////////////////////////
///////////////////////////////////////////////////////////////////////
let checkbox;

let rows = 2; //Y --> DOWN-WARDS
let cols = 2; //X --> RIGHT-WARDS
let zett = 2; //Z --> IN-WARDS


function setup() {
  var canvas = createCanvas(_width, _height);
  canvas.parent('sketch-holder');
  
  checkbox = createCheckbox('ISOMETRIC', false);
  checkbox.changed(myCheckedEvent);

  sel = createSelect();
  sel.option('FCC');
  sel.option('');
  sel.selected('');
  sel.changed(makeFCC);


for (let vec=0; vec < 3; vec++){
  PointsInputs[vec] = [];
  for (let i=0; i < 3; i++){
    PointsInputs[vec][i] = createInput(vec + i*3.3);
    PointsInputs[vec][i].position(_width+20 + vec*40, _height+65 + i*30);
  }
}


for (let atom=0; atom < AtomsNumber; atom++){
  AtomsInputs[atom] = [];
  for (let i=0; i < 3; i++){
    AtomsInputs[atom][i] = createInput(atom + i*3.3);
    AtomsInputs[atom][i].position(_height + 60 + i*30, _width + 100+atom*30);
  }
}

  button = createButton('submit');
  button.position(_width / 2, _height + 500);
  button.mousePressed(greet);

greet();
}



function draw() {
  background(0);
  translate(posX, posY);

  let projected = [];
  proj3D(points, projected);
  makeSpheres(projected, 1);

  for (let atom = 0; atom < AtomsNumber; atom++){
    let projectedAtoms = [];
    proj3D(pointsAtoms[atom], projectedAtoms);
    makeSpheres(projectedAtoms, 16, AtomsColors[atom]);
  }

  // Connecting
  makeConnections(projected);
  
  if (mouseIsPressed === true) {
    if (mouseButton === CENTER) {
      posX = mouseX;
      posY = mouseY;
      }
    if (mouseButton === LEFT) {
      angle = mouseX/_width;
      }
  }
}


function mouseWheel(event) {
  dist += event.delta / 100;
}

function myCheckedEvent() {
  if (checkbox.checked()) {
    ISO = true;
  } else {
    ISO = false;
  }
}