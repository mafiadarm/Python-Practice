decode = function(b) {
    b = b.replace(/\n/g, "");
    var a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890+/";
    var c, d = [], e = [], f = [];
    for (c = 0; b.length > c; c += 4)
        e[0] = a.indexOf(b.charAt(c)),
        e[1] = a.indexOf(b.charAt(c + 1)),
        e[2] = a.indexOf(b.charAt(c + 2)),
        e[3] = a.indexOf(b.charAt(c + 3)),
        f[0] = e[0] << 2 | e[1] >> 4,
        f[1] = (15 & e[1]) << 4 | e[2] >> 2,
        f[2] = (3 & e[2]) << 6 | e[3],
        d.push(f[0], f[1], f[2]);
    d = d.slice(0, d.length - d.length % 16);
    return d
    };

d = function (a) {
    try {
        return unescape(encodeURIComponent(a))
    } catch (b) {
        throw  "Error on UTF-8 encode"
    }
};

j = function (a, b) {
    var c, e = [];
    for (b || (a = d(a)),
             c = 0; a.length > c; c++)
        e[c] = a.charCodeAt(c);
    return e
};

O = function(a) {
        function b(a, b) {
            return a << b | a >>> 32 - b
        }
        function c(a, b) {
            var c, d, e, f, g;
            return e = 2147483648 & a,
            f = 2147483648 & b,
            c = 1073741824 & a,
            d = 1073741824 & b,
            g = (1073741823 & a) + (1073741823 & b),
            c & d ? 2147483648 ^ g ^ e ^ f : c | d ? 1073741824 & g ? 3221225472 ^ g ^ e ^ f : 1073741824 ^ g ^ e ^ f : g ^ e ^ f
        }
        function d(a, b, c) {
            return a & b | ~a & c
        }
        function e(a, b, c) {
            return a & c | b & ~c
        }
        function f(a, b, c) {
            return a ^ b ^ c
        }
        function g(a, b, c) {
            return b ^ (a | ~c)
        }
        function h(a, e, f, g, h, i, j) {
            return a = c(a, c(c(d(e, f, g), h), j)),
            c(b(a, i), e)
        }
        function i(a, d, f, g, h, i, j) {
            return a = c(a, c(c(e(d, f, g), h), j)),
            c(b(a, i), d)
        }
        function j(a, d, e, g, h, i, j) {
            return a = c(a, c(c(f(d, e, g), h), j)),
            c(b(a, i), d)
        }
        function k(a, d, e, f, h, i, j) {
            return a = c(a, c(c(g(d, e, f), h), j)),
            c(b(a, i), d)
        }
        function l(a) {
            for (var b, c = a.length, d = c + 8, e = (d - d % 64) / 64, f = 16 * (e + 1), g = [], h = 0, i = 0; c > i; )
                b = (i - i % 4) / 4,
                h = 8 * (i % 4),
                g[b] = g[b] | a[i] << h,
                i++;
            return b = (i - i % 4) / 4,
            h = 8 * (i % 4),
            g[b] = g[b] | 128 << h,
            g[f - 2] = c << 3,
            g[f - 1] = c >>> 29,
            g
        }
        function m(a) {
            var b, c, d = [];
            for (c = 0; 3 >= c; c++)
                b = 255 & a >>> 8 * c,
                d = d.concat(b);
            return d
        }
        var n, o, p, q, r, s, t, u, v, w = [], x = z("67452301efcdab8998badcfe10325476d76aa478e8c7b756242070dbc1bdceeef57c0faf4787c62aa8304613fd469501698098d88b44f7afffff5bb1895cd7be6b901122fd987193a679438e49b40821f61e2562c040b340265e5a51e9b6c7aad62f105d02441453d8a1e681e7d3fbc821e1cde6c33707d6f4d50d87455a14eda9e3e905fcefa3f8676f02d98d2a4c8afffa39428771f6816d9d6122fde5380ca4beea444bdecfa9f6bb4b60bebfbc70289b7ec6eaa127fad4ef308504881d05d9d4d039e6db99e51fa27cf8c4ac5665f4292244432aff97ab9423a7fc93a039655b59c38f0ccc92ffeff47d85845dd16fa87e4ffe2ce6e0a30143144e0811a1f7537e82bd3af2352ad7d2bbeb86d391", 8);
        for (w = l(a),
        s = x[0],
        t = x[1],
        u = x[2],
        v = x[3],
        n = 0; w.length > n; n += 16)
            o = s,
            p = t,
            q = u,
            r = v,
            s = h(s, t, u, v, w[n + 0], 7, x[4]),
            v = h(v, s, t, u, w[n + 1], 12, x[5]),
            u = h(u, v, s, t, w[n + 2], 17, x[6]),
            t = h(t, u, v, s, w[n + 3], 22, x[7]),
            s = h(s, t, u, v, w[n + 4], 7, x[8]),
            v = h(v, s, t, u, w[n + 5], 12, x[9]),
            u = h(u, v, s, t, w[n + 6], 17, x[10]),
            t = h(t, u, v, s, w[n + 7], 22, x[11]),
            s = h(s, t, u, v, w[n + 8], 7, x[12]),
            v = h(v, s, t, u, w[n + 9], 12, x[13]),
            u = h(u, v, s, t, w[n + 10], 17, x[14]),
            t = h(t, u, v, s, w[n + 11], 22, x[15]),
            s = h(s, t, u, v, w[n + 12], 7, x[16]),
            v = h(v, s, t, u, w[n + 13], 12, x[17]),
            u = h(u, v, s, t, w[n + 14], 17, x[18]),
            t = h(t, u, v, s, w[n + 15], 22, x[19]),
            s = i(s, t, u, v, w[n + 1], 5, x[20]),
            v = i(v, s, t, u, w[n + 6], 9, x[21]),
            u = i(u, v, s, t, w[n + 11], 14, x[22]),
            t = i(t, u, v, s, w[n + 0], 20, x[23]),
            s = i(s, t, u, v, w[n + 5], 5, x[24]),
            v = i(v, s, t, u, w[n + 10], 9, x[25]),
            u = i(u, v, s, t, w[n + 15], 14, x[26]),
            t = i(t, u, v, s, w[n + 4], 20, x[27]),
            s = i(s, t, u, v, w[n + 9], 5, x[28]),
            v = i(v, s, t, u, w[n + 14], 9, x[29]),
            u = i(u, v, s, t, w[n + 3], 14, x[30]),
            t = i(t, u, v, s, w[n + 8], 20, x[31]),
            s = i(s, t, u, v, w[n + 13], 5, x[32]),
            v = i(v, s, t, u, w[n + 2], 9, x[33]),
            u = i(u, v, s, t, w[n + 7], 14, x[34]),
            t = i(t, u, v, s, w[n + 12], 20, x[35]),
            s = j(s, t, u, v, w[n + 5], 4, x[36]),
            v = j(v, s, t, u, w[n + 8], 11, x[37]),
            u = j(u, v, s, t, w[n + 11], 16, x[38]),
            t = j(t, u, v, s, w[n + 14], 23, x[39]),
            s = j(s, t, u, v, w[n + 1], 4, x[40]),
            v = j(v, s, t, u, w[n + 4], 11, x[41]),
            u = j(u, v, s, t, w[n + 7], 16, x[42]),
            t = j(t, u, v, s, w[n + 10], 23, x[43]),
            s = j(s, t, u, v, w[n + 13], 4, x[44]),
            v = j(v, s, t, u, w[n + 0], 11, x[45]),
            u = j(u, v, s, t, w[n + 3], 16, x[46]),
            t = j(t, u, v, s, w[n + 6], 23, x[47]),
            s = j(s, t, u, v, w[n + 9], 4, x[48]),
            v = j(v, s, t, u, w[n + 12], 11, x[49]),
            u = j(u, v, s, t, w[n + 15], 16, x[50]),
            t = j(t, u, v, s, w[n + 2], 23, x[51]),
            s = k(s, t, u, v, w[n + 0], 6, x[52]),
            v = k(v, s, t, u, w[n + 7], 10, x[53]),
            u = k(u, v, s, t, w[n + 14], 15, x[54]),
            t = k(t, u, v, s, w[n + 5], 21, x[55]),
            s = k(s, t, u, v, w[n + 12], 6, x[56]),
            v = k(v, s, t, u, w[n + 3], 10, x[57]),
            u = k(u, v, s, t, w[n + 10], 15, x[58]),
            t = k(t, u, v, s, w[n + 1], 21, x[59]),
            s = k(s, t, u, v, w[n + 8], 6, x[60]),
            v = k(v, s, t, u, w[n + 15], 10, x[61]),
            u = k(u, v, s, t, w[n + 6], 15, x[62]),
            t = k(t, u, v, s, w[n + 13], 21, x[63]),
            s = k(s, t, u, v, w[n + 4], 6, x[64]),
            v = k(v, s, t, u, w[n + 11], 10, x[65]),
            u = k(u, v, s, t, w[n + 2], 15, x[66]),
            t = k(t, u, v, s, w[n + 9], 21, x[67]),
            s = c(s, o),
            t = c(t, p),
            u = c(u, q),
            v = c(v, r);
        return m(s).concat(m(t), m(u), m(v))
    };

m = function(c, d) {
    // ab都是固定值，就直接声明
        var a = 14;
        var b = 8;
        var e, f = a >= 12 ? 3 : 2, g = [], h = [], i = [], j = [], k = c.concat(d);
        for (i[0] = O(k),
        j = i[0],
        e = 1; f > e; e++)
            i[e] = O(i[e - 1].concat(k)),
            j = j.concat(i[e]);
        return g = j.slice(0, 4 * b),
        h = j.slice(4 * b, 4 * b + 16),
        {
            key: g,
            iv: h
        }
    };

// N是主函数，根据这个主函数去找所有的变量
N = function(a, b, c) {
    var d = decode(a)
      , e = d.slice(8, 16)
      , f = m(j(b, c), e)
      , g = f.key
      , h = f.iv;
    return d = d.slice(16, d.length), a = o(d, g, h, c)
};

c = !1;

o = function(a, b, c, d) {
        b = w(b);
        var f, h = a.length / 16, i = [], j = [], k = "";
        for (f = 0; h > f; f++)
            i.push(a.slice(16 * f, 16 * (f + 1)));
        for (f = i.length - 1; f >= 0; f--)
            j[f] = q(i[f], b),
            j[f] = 0 === f ? v(j[f], c) : v(j[f], i[f - 1]);
        for (f = 0; h - 1 > f; f++)
            k += g(j[f]);
        return k += g(j[f], !0),
        d ? k : e(k)
    };


w = function(c) {
    var a = 14;
    var b = 8;
    var d, e, f, g, h = [], i = [], j = [];
    for (d = 0; b > d; d++)
        e = [c[4 * d], c[4 * d + 1], c[4 * d + 2], c[4 * d + 3]],
        h[d] = e;
    for (d = b; 4 * (a + 1) > d; d++) {
        for (h[d] = [],
        f = 0; 4 > f; f++)
            i[f] = h[d - 1][f];
        for (0 === d % b ? (i = x(y(i)),
        i[0] ^= F[d / b - 1]) : b > 6 && 4 === d % b && (i = x(i)),
        f = 0; 4 > f; f++)
            h[d][f] = h[d - b][f] ^ i[f]
    }
    for (d = 0; a + 1 > d; d++)
        for (j[d] = [],
        g = 0; 4 > g; g++)
            j[d].push(h[4 * d + g][0], h[4 * d + g][1], h[4 * d + g][2], h[4 * d + g][3]);
    return j
    };

y = function(a) {
        var b, c = a[0];
        for (b = 0; 4 > b; b++)
            a[b] = a[b + 1];
        return a[3] = c,
        a
    };

x = function(a) {
        for (var b = 0; 4 > b; b++)
            a[b] = D[a[b]];
        //因为D在单步进入后没有方法，发现是个数组，在局部内没有定义就在全局去找
        return a
    };

z = function(a, b) {
        var c, d = [];
        for (c = 0; a.length > c; c += b)
            d[c / b] = parseInt(a.substr(c, b), 16);
        return d
    };

A = function(a) {
        var b, c = [];
        for (b = 0; a.length > b; b++)
            c[a[b]] = b;
        return c
    };

D = z("637c777bf26b6fc53001672bfed7ab76ca82c97dfa5947f0add4a2af9ca472c0b7fd9326363ff7cc34a5e5f171d8311504c723c31896059a071280e2eb27b27509832c1a1b6e5aa0523bd6b329e32f8453d100ed20fcb15b6acbbe394a4c58cfd0efaafb434d338545f9027f503c9fa851a3408f929d38f5bcb6da2110fff3d2cd0c13ec5f974417c4a77e3d645d197360814fdc222a908846eeb814de5e0bdbe0323a0a4906245cc2d3ac629195e479e7c8376d8dd54ea96c56f4ea657aae08ba78252e1ca6b4c6e8dd741f4bbd8b8a703eb5664803f60e613557b986c11d9ee1f8981169d98e949b1e87e9ce5528df8ca1890dbfe6426841992d0fb054bb16", 2);
F = z("01020408102040801b366cd8ab4d9a2f5ebc63c697356ad4b37dfaefc591", 2);
E = A(D);


q = function(b, d) {
    var a = 14;
    c = !0;
    var e, f = u(b, d, a);
    for (e = a - 1; e > -1; e--)
        f = s(f),
        f = r(f),
        f = u(f, d, e),
        e > 0 && (f = t(f));
    return f
    };

u = function(a, b, c) {
        var d, e = [];
        for (d = 0; 16 > d; d++)
            e[d] = a[d] ^ b[c][d];
        return e
    };

s = function(a) {
        var b, d = [], e = c ? [0, 13, 10, 7, 4, 1, 14, 11, 8, 5, 2, 15, 12, 9, 6, 3] : [0, 5, 10, 15, 4, 9, 14, 3, 8, 13, 2, 7, 12, 1, 6, 11];
        for (b = 0; 16 > b; b++)
            d[b] = a[e[b]];
        return d
    };

r = function(a) {
        var b, d = c ? E : D, e = [];
        for (b = 0; 16 > b; b++)
            e[b] = d[a[b]];
        return e
    };

t = function(a) {
        var b, d = [];
        if (c)
            for (b = 0; 4 > b; b++)
                d[4 * b] = L[a[4 * b]] ^ J[a[1 + 4 * b]] ^ K[a[2 + 4 * b]] ^ I[a[3 + 4 * b]],
                d[1 + 4 * b] = I[a[4 * b]] ^ L[a[1 + 4 * b]] ^ J[a[2 + 4 * b]] ^ K[a[3 + 4 * b]],
                d[2 + 4 * b] = K[a[4 * b]] ^ I[a[1 + 4 * b]] ^ L[a[2 + 4 * b]] ^ J[a[3 + 4 * b]],
                d[3 + 4 * b] = J[a[4 * b]] ^ K[a[1 + 4 * b]] ^ I[a[2 + 4 * b]] ^ L[a[3 + 4 * b]];
        else
            for (b = 0; 4 > b; b++)
                d[4 * b] = G[a[4 * b]] ^ H[a[1 + 4 * b]] ^ a[2 + 4 * b] ^ a[3 + 4 * b],
                d[1 + 4 * b] = a[4 * b] ^ G[a[1 + 4 * b]] ^ H[a[2 + 4 * b]] ^ a[3 + 4 * b],
                d[2 + 4 * b] = a[4 * b] ^ a[1 + 4 * b] ^ G[a[2 + 4 * b]] ^ H[a[3 + 4 * b]],
                d[3 + 4 * b] = H[a[4 * b]] ^ a[1 + 4 * b] ^ a[2 + 4 * b] ^ G[a[3 + 4 * b]];
        return d
    };

G = C(2);
H = C(3);
I = C(9);
J = C(11);
K = C(13);
L = C(14);

C = function(a) {
    var b, c = [];
    for (b = 0; 256 > b; b++)
        c[b] = B(a, b);
    return c
};

B = function(a, b) {
    var c, d;
    for (d = 0,
    c = 0; 8 > c; c++)
        d = 1 === (1 & b) ? d ^ a : d,
        a = a > 127 ? 283 ^ a << 1 : a << 1,
        b >>>= 1;
    return d
};

v = function(a, b) {
    var c, d = [];
    for (c = 0; 16 > c; c++)
        d[c] = a[c] ^ b[c];
    return d
};

g = function(a, b) {
        var c, d, e = "";
        if (b) {
            if (c = a[15],
            c > 16)
                throw "Decryption error: Maybe bad key";
            if (16 === c)
                return "";
            for (d = 0; 16 - c > d; d++)
                e += String.fromCharCode(a[d])
        } else
            for (d = 0; 16 > d; d++)
                e += String.fromCharCode(a[d]);
        return e
    };

e = function(a) {
        try {
            return decodeURIComponent(escape(a))
        } catch (b) {
            throw "Bad Key"
        }
    }