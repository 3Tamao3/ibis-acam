using System;

class Ceaser
{
  static void Main(string[] args)
  {
      Console.WriteLine("Gib ein text ein: ");
      string userInput = "";

      while (userInput.Length < 9)
      {
          Console.WriteLine("Mindestens 9 Buchstaben");
          userInput = Console.ReadLine();
      }

      foreach (var value in userInput)
      {
        int ascii = (int)value;

        ascii += 10;
        if (ascii > 90)
        {
            ascii -= 26;
        }

        char decrypted = (char)ascii;
        Console.Write(decrypted);
      }
      Console.WriteLine();
  }
}
