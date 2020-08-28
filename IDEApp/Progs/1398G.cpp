/*
* @Author: dnhirapara
*/
#include <bits/stdc++.h>

using namespace std;

/************defination************/

#define endl "\n"
#define log(x) cout << __LINE__ << ": " << #x << " -> " << (x) << endl;
#define ll long long int
#define ull unsigned long long int
const int MAX = 200006;
const double PI = acos(-1);
typedef complex<double> base;
void fft(vector<base> &a, bool invert)
{
    int n = (int)a.size();
    for (int i = 1, j = 0; i < n; i++)
    {
        int bit = (n >> 1);
        for (; j & bit; bit >>= 1)
            j ^= bit;
        j ^= bit;
        if (i < j)
            swap(a[i], a[j]);
    }
    for (int len = 2; len <= n; len <<= 1)
    {
        double ang = 2 * PI / len * (invert ? -1 : 1);
        base wlen(cos(ang), sin(ang));
        for (int i = 0; i < n; i += len)
        {
            base w(1);
            for (int j = 0; j < (len / 2); j++)
            {
                base u = a[i + j], v = a[i + j + (len / 2)] * w;
                a[i + j] = u + v;
                a[i + j + (len / 2)] = u - v;
                if (invert)
                {
                    a[i + j] /= 2;
                    a[i + j + (len / 2)] /= 2;
                }
                w *= wlen;
            }
        }
    }
}

vector<int> multiply(const vector<int> &a, const vector<int> &b)
{
    vector<base> A(a.begin(), a.end());
    vector<base> B(b.begin(), b.end());
    size_t n = 1;
    while (n < (max(A.size(), B.size())))
    {
        n <<= 1;
    }
    n <<= 1;
    A.resize(n);
    B.resize(n);
    vector<base> res(n);
    fft(A, false);
    fft(B, false);
    for (int i = 0; i < n; i++)
    {
        res[i] = A[i] * B[i];
    }
    fft(res, true);
    vector<int> _res(n);
    for (int i = 0; i < n; i++)
    {
        _res[i] = (int)(res[i].real() + 0.5);
        // cout << res[i] << endl;
    }
    return _res;
}
//@time comp :
//@space comp :
int main()
{
    // ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    // cin.ignore(); must be there when using getline(cin, s)
    ll tc = 1;
    // cin >> tc;
    while (tc--)
    {
        int n, x, y;
        cin >> n >> x >> y;
        vector<int> a(x + 1), b(x + 1), ans(10 * MAX, -1);
        int k;
        // cout << n << x << y;
        for (int i = 0; i < n + 1; i++)
        {
            cin >> k;
            a[k] = 1;
            b[x - k] = 1;
        }
        auto res = multiply(a, b);
        int maxi_size = 10 * MAX;
        for (int i = x + 1; i < maxi_size; i++)
        {
            if (i >= res.size())
                break;
            if (res[i] > 0)
            {
                int len = 2 * ((i - x) + y);
                for (int j = len; j < maxi_size; j += len)
                {
                    ans[j] = len;
                }
            }
        }
        int q;
        cin >> q;
        while (q--)
        {
            cin >> k;
            cout << ans[k] << " ";
        }
    }
    return 0;
}