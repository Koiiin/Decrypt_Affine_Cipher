# Affine Cipher Brute Force Decryption

This Python script attempts to decrypt an Affine Cipher-encrypted text by brute-forcing all possible key values.

## What is the Affine Cipher?

The Affine Cipher is a monoalphabetic substitution cipher that encrypts letters using the formula:

$$
E(x) = (a \times x + b) \mod 26
$$

Where:

- \(x\) is the letter index (A = 0, B = 1, ..., Z = 25).
- \(a\) and \(b\) are keys chosen by the user.
- \(a\) must be coprime with 26 to be invertible.

### Decryption Formula

To decrypt, the inverse of \(a\) modulo 26 (denoted as \(a^{-1}\)) is used:

$$
D(y) = a^{-1} \times (y - b) \mod 26
$$

Where:

- \(y\) is the encrypted letter index.

## How It Works

- This script first calculates \(a^{-1}\) using a brute-force method.
- It then applies the decryption formula to each character in the ciphertext.
- A brute-force function tries all possible \((a, b)\) pairs and prints possible decrypted texts.

