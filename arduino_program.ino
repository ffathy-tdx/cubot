const int dirPins[] = {2, 4, 6, 8, 10, 12};
const int stepPins[] = {3, 5, 7, 9, 11, 13};
const int enablePins[] = {14, 15, 16, 17, 18, 19};
const int numMotors = 6;
char receivedCommand = '\0';


void enableMotor(int motor);
void disableMotor(int motor);
void moveMotor(int motor);

void setup()
{
 
  for (int i = 0; i < numMotors; i++)
  {
    pinMode(dirPins[i], OUTPUT);
    pinMode(stepPins[i], OUTPUT);
    pinMode(enablePins[i], OUTPUT);
  }

  
  for (int i = 0; i < numMotors; i++)
  {
    disableMotor(i);
  }


  Serial.begin(9600);
}
int f=1;
void loop()
{
  if (Serial.available())
  {f
   
    receivedCommand = Serial.read();

   
    switch (receivedCommand)
    {
      case 'u':
        
        enableMotor(0); 
        moveMotor(0 , 50);    
        disableMotor(0); 
        break;

      case 'l':
      
    

        enableMotor(1);  
        moveMotor(1,50);    
        disableMotor(1); 
        break;

      case 'r':
       

      
        enableMotor(2);  
        moveMotor(2,50);   
        disableMotor(2); 
        break;

      case 'f':

        enableMotor(3);  
        moveMotor(3,20);    
        disableMotor(3);
 
        break;
        
      case 'b':
        

        enableMotor(4);  
        moveMotor(4,50);   
        disableMotor(4); 

        break;
        
      case 'd':

        
        enableMotor(5); 
        moveMotor(5,50);    
        disableMotor(5); 
 
       break;



      default:
        
        Serial.println("Invalid command");
        break;
    }

    
    receivedCommand = '\0';
  }
  delay(100);
}

void enableMotor(int motor)
{
  digitalWrite(enablePins[motor], LOW); 
}

void disableMotor(int motor)
{
  digitalWrite(enablePins[motor], HIGH); 
}

void moveMotor(int motor, int steps)
{
 
  digitalWrite(dirPins[motor], HIGH);

  
  for (int step = 0; step < steps; step++)
  {
    digitalWrite(stepPins[motor], HIGH);
    delayMicroseconds(1000);
    digitalWrite(stepPins[motor], LOW);
    delayMicroseconds(1000);
  }
}
//