# Pascal
Pascal
program calculator;
uses
  Crt;

var
  choice: integer;

procedure LaunchCalculator(choice: integer);
var
  number1, number2: integer;
begin
  write('Write first number: ');
  readln(number1);
  write('Write second number: ');
  readln(number2);

  case choice of
    1: writeln(number1, ' + ', number2, ' = ', number1 + number2);
    2: writeln(number1, ' - ', number2, ' = ', number1 - number2);
    3: writeln(number1, ' * ', number2, ' = ', number1 * number2);
    4: writeln(number1, ' / ', number2, ' = ', number1 / number2);
  end;
end;

begin
  repeat
    writeln('1 - Add, 2 - Sub, 3 - Mul, 4 - Div, 5 - Quit');
    readln(choice);
    ClrScr;
    if choice <> 5 then
      LaunchCalculator(choice);
  until choice = 5;
  writeln('Thanks for using my calculator :D');
end.