let ct = BigInt(0)
let g = BigInt(0)
let p = BigInt(0)
let q = BigInt(0)
let n = BigInt(0)
let lambda = BigInt(0)
let mu = BigInt(0)

function gcd(a, b) {
    if (b == 0) {
        return BigInt(a);
    }
    return gcd(b, BigInt(a) % BigInt(b));
}

function lcm(x, y) {
    return BigInt(x * y) / gcd(x, y)
}

function loudEncrypt() {
    // Set up program.
    let explaition = document.getElementById("firstValue")
    let pt = BigInt(document.getElementById("pt").value)
    g = BigInt(document.getElementById("g").value)
    p = document.getElementById("p").value
    q = document.getElementById("q").value
    n = p * q

    let r = Math.random() * n
    r = BigInt(Math.ceil(r))
    while (gcd(n, r) != 1) {
        r = Math.random() * n
        r = BigInt(Math.ceil(r)) // we do not want zero anyways.
    }
    r = BigInt(r)
    explaition.innerHTML += "First let's pick a random r. We want this r to exist within 0 < r < n and have the following property: gcd(r, n) = 1 <br>"
    explaition.innerHTML += "Let's use the r " + r + "<br>"
    explaition.innerHTML += "Next we will want to compute the following <br> g^pt * r^n."
    let cipherText = BigInt(((BigInt(g ** pt)) * BigInt((r ** BigInt(n)))))
    explaition.innerHTML += "Giving us the resulting cipher text: " + cipherText + "<br>"
    explaition.innerHTML += "The last step of this process is taking solving ct = ct mod n^2 <br>"
    cipherText = cipherText % BigInt(n ** 2)
    ct = cipherText
    explaition.innerHTML += "Resulting in our final answer of " + cipherText
    // Remove visibility
    document.getElementById("descP").style.visibility = "hidden"

    document.getElementById("dec").style.visibility = "visible"
    document.getElementById("AddingEnc").style.visibility = "visible"
    document.getElementById("result").innerHTML = "New Cipher text: " + ct + "<br>"
}

function modInverse(x, y) {
    x = BigInt(x)
    y = BigInt(y)
    for (let i = 0; i < y; i++) {
        i = BigInt(i)
        if (((x % y) * (i % y)) % y == BigInt(1)) {
            return i
        }
    }
    return -1
}

function decrypt() {
    write = document.getElementById("resultDec")
    write.innerHTML += "First we will want to computer the least common multiple of (p - 1, q - 1)<br>"
    lambda = BigInt(lcm(p - 1, q - 1))
    write.innerHTML += "lcm = " + lambda + "<br>"
    let pt = L(BigInt(g ** lambda))
    write.innerHTML += "Next we want to compute g^lcm = x<br>"
    write.innerHTML += "x = " + BigInt(g ** lambda)
    write.innerHTML += "<br>Afterwards, we want to compute (x - 1)/n = " + pt + "<br>"
    write.innerHTML += "Ensure our value exists within our modulo group n^2.<br>"
    pt = pt % BigInt(n ** 2)
    mu = modInverse(pt, n)
    write.innerHTML += "Next we will want to compute the modulo inverse of this value. This is our mu = " + mu + "<br>"
    pt = BigInt(BigInt(ct) ** BigInt(lambda)) % BigInt(n ** 2)
    write.innerHTML += "Now with that mu we can begin deciphering. First we will solve ct^lcm mod n^2 = " + pt + " = y<br>"
    pt = BigInt(L(pt)) * mu
    pt = BigInt(pt) % BigInt(n)
    write.innerHTML += "Now we will want to compute (((y - 1)/n) * mu) mod n = " + pt + "<br>"
    write.innerHTML += "Successfully giving us our plain text result of " + pt
    console.log(pt)

    document.getElementById("AddingEnc").style.visibility = "hidden"
}

function L(mu) {
    x = mu - BigInt(1)
    x /= BigInt(n)
    return BigInt(x)
}

function Encrypt(pt) {
    let r = Math.random() * n
    r = Math.ceil(r)
    while (gcd(n, r) != 1) {
        r = Math.random() * n
        r = BigInt(Math.ceil(r)) // we do not want zero anyways.
    }
    r = BigInt(r)
    let cipherText = BigInt(((BigInt(g ** BigInt(pt))) * BigInt((r ** BigInt(n)))))
    cipherText = BigInt(cipherText) % BigInt(n ** 2)
    return cipherText
}

function homomorphicAddition() {
    pt = document.getElementById("ptPrime").value

    cipherText = Encrypt(pt)
    document.getElementById("result").innerHTML += "E(pt) = " + cipherText + "<br>"
    document.getElementById("result").innerHTML += "Operation: " + ct + " * " + cipherText + " = "
    ct = (ct * cipherText)
    document.getElementById("result").innerHTML += ct + "<br>"
}
