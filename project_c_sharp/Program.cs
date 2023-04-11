using project_c_sharp;
using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TARpv22_FirstCsharp
{
    public class start
    {
        public static void Main(string[] args)
        {
            //string paev = " ";
            //Random rnd = new Random();
            //for (int i = 0; i < 10; i++)
            //{
            //    int nr = rnd.Next(1, 7);
            //    Console.WriteLine(nr);
            //    switch (nr)
            //    {
            //        case 1: paev = "Esmaspaev"; break;
            //        case 2: paev = "Teisipäev"; break;
            //        case 3: paev = "Kolmapäev"; break;
            //        case 4: paev = "Neljapäev"; break;
            //        case 5: paev = "Reede"; break;
            //        case 6: paev = "Lauapäev"; break;
            //        case 7: paev = "Pühapäev"; break;
            //        default:
            //            paev = "Tundmatu päev";
            //            break;
            //    }
            //    Console.WriteLine(paev);
            //}
            //int j = 0;
            //while (j < 10)
            //{
            //    Console.WriteLine(paev);
            //    j++;
            //}
            //do
            //{
            //    Console.WriteLine(paev);
            //    j--;
            //} while (j != 0);
            //Console.WriteLine(paev);
            //int[] arvud = new int[10];
            //for (int i = 0; i < arvud.Length; i++)
            //{
            //    arvud[i] = rnd.Next(-100, 100);
            //}

            //foreach (int item in arvud)
            //{
            //    if (item < 0)
            //    {
            //        Console.Beep();
            //    }
            //    Console.WriteLine(item);
            //}
            //Console.WriteLine("Tere tulemast!\n Mis on sinu nimi?");
            //string eesnimi = Console.ReadLine();
            //Console.WriteLine("Tere " + eesnimi);
            //Console.WriteLine("Arv1");
            //int arv1 = int.Parse(Console.ReadLine());
            //Console.WriteLine("Arv2");
            //int arv2 = int.Parse(Console.ReadLine());
            //Console.WriteLine("Tehe");
            //char tehe = char.Parse(Console.ReadLine());
            //if (tehe == '+')
            //{
            //    Console.WriteLine("Arvude {0} ja {1} summa võrdub {2}", arv1, arv2, arv1 + arv2);
            //}
            //else if (tehe == '-')
            //{
            //    Console.WriteLine("Arvude {0} ja {1} summa võrdub {2}", arv1, arv2, arv1 - arv2);
            //}

            //Console.WriteLine("Mis sinu nimi on");
            //string nimi=Console.ReadLine();
            //if (nimi.ToUpper()=="JUKU")
            //{
            //Console.WriteLine("Kui vana sa on?");
            //int arv = int.Parse(Console.ReadLine());
            //if (arv <= 6)
            //{
            //    Console.WriteLine("Sinu pilet on tasuta");
            //}
            //else if (arv > 6 && arv < 14)
            //{
            //    Console.WriteLine("Sul on lastepilet.");
            //}
            //else if (arv > 15 && arv < 65)
            //{
            //    Console.WriteLine("Sul täispilet");
            //}
            //else if (arv > 65)
            //{
            //    Console.WriteLine("Sul on sooduspilet");
            //}
            //else if (arv<0 || arv>100)
            //{
            //    Console.WriteLine("Viga!");
            //}
            //}

            //Console.WriteLine("Mis on sinu nimi?");
            //string eesni1=Console.ReadLine();
            //Console.WriteLine("Aga teie?");
            //string eesni2=Console.ReadLine();
            //if (eesni1 == "Anton" && eesni2 == "Katja" || eesni2=="Anton" && eesni1=="Katja")
            //{
            //    Console.WriteLine($"{eesni1} ja {eesni2}, täna on pinginaabri");
            //}
            //else
            //{
            //    Console.WriteLine("Mite midagi.");
            //}

            //Задание 1

            //int arree = 0;
            //Random rnd = new Random();
            //int n = rnd.Next(-100, 100);
            //int m = rnd.Next(-100, 100);
            //Console.WriteLine($"N-" + n);
            //Console.WriteLine($"M-" + m);
            //if (n > 0 && m > 0)

            //    if (n > m)
            //    {
            //        Console.WriteLine("Summ" + "-" + (n - m));
            //        arree = Math.Abs(n - m);
            //    }
            //    else if (n < m)
            //    {
            //        Console.WriteLine("Summ" + "-" + (m - n));
            //        arree = Math.Abs(m - n);
            //    }
            //    else if (n < 0 && m > 0)
            //    {
            //        arree = Math.Abs(n) + m;
            //    }
            //    else if (m < 0 && n > 0)
            //    {
            //        arree = Math.Abs(m) + n;
            //    }
            //    else if (m < 0 && n < 0)
            //    {
            //        arree = Math.Abs(n) + m;
            //    }
            //    else
            //    {
            //        arree = Math.Abs(m + n);
            //    }
            //int[] item = new int[arree];
            //for (int i = 0; i < item.Length; i++)
            //{
            //    Console.WriteLine(i);
            //    Console.WriteLine(i ^ i);
            //}


            //string nimi = "Python";
            //Alamprog.Tere(nimi);

            //int a = 12;
            //int b = 13;
            //int vastus = Alamprog.Korruta(a, b);
            //Console.WriteLine(vastus);
            //Console.WriteLine(Alamprog.Korruta(5, 6));

            //Console.WriteLine("Sisseta esimene arv: ");
            //int a = Convert.ToInt32(Console.ReadLine());
            //Console.WriteLine("Sisseta teine arv: ");
            //int b = Convert.ToInt32(Console.ReadLine());
            //int n = 2;
            //int vastus = Alamprog.Keskmine(n, a, b);
            //Console.WriteLine("\nKeskmine arv on "+vastus);

            //double a = 10;
            //double b = 20;
            //double vastus = Alamprog.Jagata(a, b);
            //Console.WriteLine(vastus);

            //int a = 2;
            //int b = 4;
            //char tehe = '+';
            //string vastus = Alamprog.Klakulaator(a, b, tehe);
            //Console.WriteLine(vastus);

            //int b = 3;
            //string vastus = Alamprog.Stars(b);
            //Console.WriteLine(vastus);

            Console.WriteLine("Kui palju: ");
            int j = Convert.ToInt32(Console.ReadLine());    
            Alamprog.NStars(j);
        }
    }
}
