string wort1 = Console.ReadLine();
string wort2 = Console.ReadLine();

if (wort1.Length > 99 || wort1.Length < 1 || wort2.Length > 99 || wort2.Length < 1)
{
    Console.WriteLine("Zwischen 1-99 Char bitte");
    return;
}

if (wort1.Any(char.IsUpper) || wort2.Any(char.IsUpper))
{
  Console.WriteLine("Nur Kleinbuchstaben");
  return;
}

int maxLength = wort1.Length + wort2.Length;

for (int i = 0; i < maxLength; i++)
{
    if (i < wort1.Length)
    {
        Console.Write(wort1[i]);
    }
    if (i < wort2.Length)
    {
        Console.Write(wort2[i]);
    }
}
Console.WriteLine();

