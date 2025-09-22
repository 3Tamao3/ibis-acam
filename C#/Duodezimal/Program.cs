using System;
using System.Text;

class Program
{
    static void Main()
    {
        Random random = new Random();

        int[] numbers = new int[150];
        for (int i = 0; i < numbers.Length; i++)
        {
            numbers[i] = random.Next(1, 1000001);
        }

        Console.WriteLine("\n\n\nUNSORTIERT\n");
        PrintNumbers(numbers);

        Array.Sort(numbers);
        Console.WriteLine("\n\n\n SORTIERT (Aufsteigend)\n");
        PrintNumbers(numbers);

        Array.Reverse(numbers);
        Console.WriteLine("\n\n\n SORTIERT (Absteigend)\n");
        PrintNumbers(numbers);
    }

    static void PrintNumbers(int[] numbers)
    {
        int count = 1;
        foreach (var num in numbers)
        {
            string duodecimal = ToBase12(num);
            Console.WriteLine(count++ + ". " + num + " " + duodecimal);
        }
    }

    static string ToBase12(int number)
    {
        if (number == 0) return "0";

        const string symbols = "0123456789AB";
        StringBuilder result = new StringBuilder();

        int n = number;
        while (n > 0)
        {
            int remainder = n % 12;
            result.Insert(0, symbols[remainder]);
            n = n / 12;
        }

        return result.ToString();
    }
}

