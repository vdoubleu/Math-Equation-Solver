#include <vector>
#include <string>
#include <map>
#include <iostream>
#include <sstream>

#include "amalgamate/crow_all.h"

using namespace std;

string reverseString(string s)
{
    int len = s.length();
    string t = "";
    for (int i = len - 1; i >= 0; --i)
    {
        t += s.at(i);
    }
    return t;
}

map<int, int> makeMap(vector<int> pow, vector<int> co)
{
    int len = pow.size();
    int len2 = co.size();
    map<int, int> poly;

    // cout << "testing, pow size: " << len << " coeff size: " << len2 << endl;

    // for (int i = 0; i < len; ++i)
    // {
    //     cout << pow.at(i) << " ";
    // }
    // cout << endl;
    // for (int i = 0; i < co.size(); ++i)
    // {
    //     cout << co.at(i) << " ";
    // }
    // cout << endl;

    if (len != co.size())
    {
        cerr << "Sizes of vectors pow and co are different, pow: " << pow.size() << ", co: " << co.size() << endl;
    }
    for (int i = 0; i < len; ++i)
    {
        int p = pow.at(i);
        int c = co.at(i);
        if (poly.find(p) != poly.end())
        {
            poly[p] += c;
        }
        else
        {
            poly[p] = c;
        }
    }
    return poly;
}
string cleanString(string s)
{
    int len = s.length();
    for (int i = 0; i < len; ++i)
    {
        char c = s.at(i);
        int diff = c - '0';
        if (c != 'x' && c != '^' && c != '+' && c != '-' && (diff < 0 || diff > 9))
        {
            s.replace(i, 1, "");
            // cout << "i: " << i << endl;
            --i;
            --len;
            // cout << s << endl;
        }
    }
    cout << s << endl;
    return s;
}
int addContants(string s)
{
    int len = s.length();
    int sum = 0;
    for (int i = 0; i < len; ++i)
    {
        char c = s.at(i);
        // cout << c << endl;
        int diff = c - '0';
        if (diff >= 0 && diff <= 9)
        {
            sum += diff;
        }
    }
    return sum;
}
//called after parse Power
vector<int> parseCoeff(string s)
{
    vector<int> co;
    // ---------- parse coeff
    // cout << "running parsecoeff";
    // cout << "s: " << s << endl;
    int pos = s.find("x");
    int len = s.length();
    // cout << "pos: " << pos << endl;
    s.replace(pos, 1, "");
    --len;
    while (pos >= 0 && pos <= len)
    {
        --pos;
        string coeff = "";
        char c;
        if (pos >= 0)
        {
            c = s.at(pos);
            // cout << "pos: " << pos << endl;
            int diff = c - '0';
            int count = 0;
            while (diff >= 0 && diff <= 9)
            {
                ++count;
                coeff += c;
                // cout << coeff << endl;
                s.replace(pos, 1, "");
                // cout << "s: " << s << endl;
                --len;
                --pos;
                if (pos >= 0)
                {
                    c = s.at(pos);
                }
                else
                {
                    pos = 0;
                    break;
                }
                diff = c - '0';
                // cout << "s: " << s << endl;
            }
            if (count == 0)
            {
                coeff = "1";
            }
        }
        else
        {
            coeff = "1";
            pos=0;
        }
        coeff = reverseString(coeff);
        stringstream cof(coeff);
        int x = 0;
        cof >> x;
        if (c == '-')
        {
            x = x * -1;
        }
        co.push_back(x);

        // cout << coeff << endl;
        coeff = "";
        // cout << "pos: " << pos << endl;
        pos = s.find("x", pos);
        if (pos >= 0)
        {
            s.replace(pos, 1, "");
            --len;
        }
        // cout << "pos: " << pos << endl;
        // cout << "s: " << s << endl;
    }
    //coeff will always have one more entry than power due to constants
    co.push_back(addContants(s));
    return co;
}
map<int, int> parsePower(string s)
{
    vector<int> p;
    // ---------- parse power
    int pos = s.find("x");
    int len = s.length();
    // cout << "s: " << s << endl;
    // s.replace(pos, 1, "");
    // --len;
    while (pos >= 0 && pos < len)
    {
        string power = "";
        //has exponent
        if (pos + 1 < len && s.at(pos + 1) == '^')
        {
            ++pos;
            s.replace(pos, 1, "");
            --len;
            // ++pos;
            char c = s.at(pos);
            int diff = c - '0';
            while (diff >= 0 && diff <= 9)
            {
                power += c;
                s.replace(pos, 1, "");
                --len;
                // ++pos;
                if (pos < len)
                {
                    c = s.at(pos);
                }
                else
                {
                    break;
                }
                diff = c - '0';
                // cout << "s: " << s << endl;
            }
        }
        else
        {
            power = "1";
            ++pos;
        }
        stringstream pow(power);
        int x = 0;
        pow >> x;
        p.push_back(x);
        // cout << power << endl;
        power = "";
        pos = s.find("x", pos);
        // cout << "pos: " << pos << endl;
        // cout << "s: " << s << endl;
    }
    // ---------- done parsing power
    p.push_back(0);
    vector<int> co = parseCoeff(s);
    return makeMap(p, co);
    // for (int i = 0; i < co.size(); ++i)
    // {
    //     cout << co.at(i) << " ";
    // }
    // cout << endl;
}

int main(int argc, char *argvp[])
{
    crow::SimpleApp app;


    string s = "";
    //getline(cin, s);
    string out;


    CROW_ROUTE(app, "/calc/")
    ([](const crow::request& req){
      auto x = crow::json::load(req.body);
      if(!x)
         return crow::response(400);

    s = cleanString(s);
    // cout << s << endl;

    map<int,int> poly = parsePower(s);
    map<int, int> :: iterator itr;
    for(itr = poly.begin(); itr != poly.end(); ++itr){
        out =  "key: " + itr->first + ", value: " + itr->second << endl;
    }

    std::ostringstream os;

   os << out;
   return crow::response{os.str()};
   });

   app.port(7000).multithreaded().run();
}
