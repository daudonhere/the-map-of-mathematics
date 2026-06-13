from __future__ import annotations

import random

from mathverse.core.models import SubTopic

subtopics: list[SubTopic] = [
    SubTopic(
        title={"id": "Kriptografi", "en": "Cryptography"},
        description={
            "id": (
                "Kriptografi adalah ilmu menyembunyikan pesan dengan "
                "mengubahnya menjadi kode yang hanya dapat dibaca oleh penerima yang berwenang."
            ),
            "en": (
                "Cryptography is the science of hiding messages by "
                "transforming them into code readable only by the intended recipient."
            ),
        },
        explanation={
            "id": (
                "Caesar cipher: geser setiap huruf sebanyak n posisi — cipher paling sederhana.\n"
                "Dengan kunci 3, A\u2192D, B\u2192E, C\u2192F, ... Z\u2192C — cipher shift.\n"
                "Kriptografi modern menggunakan kunci publik dan privat (RSA) — "
                "satu kunci untuk enkripsi, kunci lain untuk dekripsi.\n"
                "Enkripsi RSA: pangkatkan plainteks m dengan e modulo n — keamanan "
                "bergantung pada sulitnya memfaktorkan bilangan besar."
            ),
            "en": (
                "Caesar cipher: shift each letter by n positions — the simplest cipher.\n"
                "With key 3, A\u2192D, B\u2192E, C\u2192F, ... Z\u2192C — shift cipher.\n"
                "Modern cryptography uses public and private keys (RSA) — "
                "one key for encryption, another for decryption.\n"
                "RSA encryption raises the plaintext message m to the power e modulo n — "
                "the security relies on the difficulty of factoring large numbers."
            ),
        },
        examples={
            "id": [
                "Caesar cipher (kunci=3):",
                "  HELLO \u2192 KHOOR",
                "",
                "RSA: kunci publik (n, e), kunci privat (n, d)",
                "  Enkripsi: c = m^e mod n",
            ],
            "en": [
                "Caesar cipher (key=3):",
                "  HELLO \u2192 KHOOR",
                "",
                "RSA: public key (n, e), private key (n, d)",
                "  Encryption: c = m^e mod n",
            ],
        },
        playground="cryptography",
    ),
    SubTopic(
        title={"id": "Coding Theory (Teori Pengkodean)", "en": "Coding Theory"},
        description={
            "id": (
                "Teori pengkodean mempelajari cara mendeteksi dan memperbaiki "
                "kesalahan dalam transmisi data dengan menambahkan redundansi."
            ),
            "en": (
                "Coding theory studies how to detect and correct "
                "errors in data transmission by adding redundancy."
            ),
        },
        explanation={
            "id": (
                "Parity bit: tambahkan bit ekstra agar jumlah bit 1 genap "
                "(even parity) — mendeteksi kesalahan satu bit.\n"
                "1011 memiliki 3 bit 1 (ganjil), jadi tambahkan 1 untuk membuatnya genap.\n"
                "Setelah parity bit ditambahkan, codeword memiliki jumlah "
                "bit 1 genap, memenuhi properti parity.\n"
                "Jarak Hamming mengukur berapa banyak posisi bit yang berbeda "
                "antara dua codeword — jarak minimum menentukan kemampuan koreksi error."
            ),
            "en": (
                "Parity bit: add an extra bit to make the total number of 1s even "
                "(even parity) — detects single-bit errors.\n"
                "1011 has 3 ones (odd), so append 1 to make the count even.\n"
                "After adding the parity bit, the codeword now has an even number "
                "of 1s, confirming the parity property.\n"
                "Hamming distance measures how many bit positions differ between two "
                "codewords — the minimum distance determines error correction capability."
            ),
        },
        examples={
            "id": [
                "Parity bit (even parity):",
                "  1011: 3 bit 1 (ganjil) \u2192 tambah 1",
                "  menjadi 10111 (4 bit 1, genap)",
                "",
                "Jarak Hamming:",
            ],
            "en": [
                "Parity bit (even parity):",
                "  1011: 3 ones (odd) \u2192 append 1",
                "  becomes 10111 (4 ones, even)",
                "",
                "Hamming distance:",
            ],
        },
        playground="coding_theory",
    ),
    SubTopic(
        title={"id": "Blockchain", "en": "Blockchain"},
        description={
            "id": (
                "Blockchain adalah rantai blok yang berisi data transaksi, "
                "dirangkai dengan hash kriptografi sehingga tidak dapat diubah."
            ),
            "en": (
                "A blockchain is a chain of blocks containing transaction data, "
                "linked with cryptographic hashes so it cannot be altered."
            ),
        },
        explanation={
            "id": (
                "Setiap blok dalam blockchain berisi data, timestamp, dan hash "
                "dari blok sebelumnya.\n"
                "Blok 1 tidak memiliki blok sebelumnya (HashPrev=0), "
                "sehingga disebut genesis block.\n"
                "Blok 2 menyimpan hash dari Blok 1, menciptakan tautan yang "
                "tidak dapat diubah.\n"
                "Proof of work membutuhkan pencarian nonce sehingga hash blok "
                "dimulai dengan sejumlah nol di depan."
            ),
            "en": (
                "Each block in a blockchain contains data, a timestamp, and the hash "
                "of the previous block.\n"
                "Block 1 has no previous block (HashPrev=0), so it is the genesis "
                "block.\n"
                "Block 2 stores the hash of Block 1, creating an immutable link.\n"
                "Proof of work requires finding a nonce such that the block's hash "
                "begins with a specified number of leading zeros."
            ),
        },
        examples={
            "id": [
                "Blok 1: [Data1 | Timestamp | HashPrev=0 | Nonce | Hash]",
                "Blok 2: [Data2 | Timestamp | HashPrev=Hash1 | Nonce | Hash]",
                "",
                "Proof of work (Bitcoin):",
                "  Cari nonce sehingga hash mulai dengan 0000...",
            ],
            "en": [
                "Block 1: [Data1 | Timestamp | HashPrev=0 | Nonce | Hash]",
                "Block 2: [Data2 | Timestamp | HashPrev=Hash1 | Nonce | Hash]",
                "",
                "Proof of work (Bitcoin):",
                "  Find nonce so hash starts with 0000...",
            ],
        },
        playground="blockchain",
    ),
    SubTopic(
        title={"id": "Error Correction (Koreksi Kesalahan)", "en": "Error Correction"},
        description={
            "id": (
                "Koreksi kesalahan memungkinkan data yang rusak saat transmisi "
                "untuk diperbaiki tanpa perlu mengirim ulang."
            ),
            "en": (
                "Error correction allows corrupted data during transmission "
                "to be repaired without needing to resend."
            ),
        },
        explanation={
            "id": (
                "Repetition code: kirim setiap bit 3 kali (111 untuk 1) "
                "— jika satu bit error, mayoritas menang.\n"
                "Enkoding: bit data asli 1 dikirim sebagai tiga salinan (111) "
                "untuk redundansi.\n"
                "Dekoding mayoritas: meskipun bit tengah rusak (101), "
                "dua bit 1 lainnya menunjukkan nilai yang benar adalah 1.\n"
                "Hamming(7,4) adalah kode koreksi error linear yang dapat "
                "mendeteksi dan memperbaiki error satu bit."
            ),
            "en": (
                "Repetition code: send each bit 3 times (111 for 1) "
                "— if one bit is wrong, majority wins.\n"
                "Encoding: the original data bit 1 is transmitted as three "
                "copies (111) for redundancy.\n"
                "Majority decoding: even though the middle bit was "
                "corrupted (101), the other two 1s indicate the correct value is 1.\n"
                "Hamming(7,4) is a linear error-correcting code that can "
                "detect and correct single-bit errors."
            ),
        },
        examples={
            "id": [
                "Repetition code (r=3):",
                "  Data: 1 \u2192 dikirim 111",
                "  Terima 101 \u2192 mayoritas 1 \u2192 perbaiki ke 1",
                "",
                "Hamming(7,4) dapat memperbaiki 1 error:",
            ],
            "en": [
                "Repetition code (r=3):",
                "  Data: 1 \u2192 send 111",
                "  Receive 101 \u2192 majority 1 \u2192 correct to 1",
                "",
                "Hamming(7,4) can correct 1 error:",
            ],
        },
        playground="error_correction",
    ),
]


def gen_question(playground: str, locale: str) -> tuple[str, str, float] | None:
    def _(en: str, id: str) -> str:
        return en if locale == "en" else id

    if playground == "cryptography":
        kind = random.choice(["caesar", "xor_cipher"])
        if kind == "caesar":
            letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            idx = random.randint(0, len(letters) - 1)
            shift = random.randint(1, 5)
            c = letters[idx]
            enc_idx = (idx + shift) % len(letters)
            enc = letters[enc_idx]
            if random.randint(0, 1):
                q = _(
                    f"Caesar cipher key={shift}: {c} \u2192 ?",
                    f"Cipher Caesar kunci={shift}: {c} \u2192 ?",
                )
                return q, enc, 0.0
            else:
                dec_idx = (enc_idx - shift) % len(letters)
                dec = letters[dec_idx]
                q = _(
                    f"Decrypt '{enc}' with key={shift}: original letter?",
                    f"Dekripsi '{enc}' dengan kunci={shift}: huruf asli?",
                )
                return q, dec, 0.0
        else:
            bit = random.randint(0, 1)
            key_bit = random.randint(0, 1)
            encrypted = bit ^ key_bit
            q = _(
                f"XOR cipher: plaintext={bit}, key={key_bit}, ciphertext=?",
                f"XOR cipher: plainteks={bit}, kunci={key_bit}, cipherteks=?",
            )
            return q, str(encrypted), encrypted

    elif playground == "coding_theory":
        kind = random.choice(["parity", "hamming_dist"])
        if kind == "parity":
            bits = [random.randint(0, 1) for _ in range(4)]
            ones = sum(bits)
            parity = 0 if ones % 2 == 0 else 1
            bits_str = "".join(str(b) for b in bits)
            q = _(
                f"Even parity bit for {bits_str} = ?",
                f"Parity bit genap untuk {bits_str} = ?",
            )
            return q, str(parity), parity
        else:
            a = [random.randint(0, 1) for _ in range(4)]
            b = [random.randint(0, 1) for _ in range(4)]
            dist = sum(1 for i in range(4) if a[i] != b[i])
            a_str = "".join(str(bit) for bit in a)
            b_str = "".join(str(bit) for bit in b)
            q = _(
                f"Hamming distance between {a_str} and {b_str} = ?",
                f"Jarak Hamming antara {a_str} dan {b_str} = ?",
            )
            return q, str(dist), dist

    elif playground == "blockchain":
        kind = random.choice(["hash_change", "nonce"])
        if kind == "hash_change":
            txt = random.choice(["Hello", "Block", "Data", "TX01", "Merkle"])
            q = _(
                f"If '{txt}' is hashed, then changed to '{txt}2', "
                f"does the hash change? (yes/no)",
                f"Jika '{txt}' di-hash, lalu diubah menjadi '{txt}2', "
                f"apakah hash berubah? (ya/tidak)",
            )
            return q, _("yes", "ya"), 0.0
        else:
            target = random.choice(["000", "0000"])
            q = _(
                f"Proof of work: find nonce so hash starts with '{target}' — "
                f"is this easy or hard? (easy/hard)",
                f"Proof of work: cari nonce agar hash mulai '{target}' — "
                f"apakah ini mudah atau sulit? (mudah/sulit)",
            )
            return q, _("hard", "sulit"), 0.0

    elif playground == "error_correction":
        kind = random.choice(["majority", "hamming_dist"])
        if kind == "majority":
            bits = [random.randint(0, 1) for _ in range(3)]
            ones = sum(bits)
            ans = 1 if ones >= 2 else 0
            bits_str = "".join(str(b) for b in bits)
            q = _(
                f"Repetition code: received {bits_str}, correct bit = ?",
                f"Repetition code: terima {bits_str}, bit yang benar = ?",
            )
            return q, str(ans), ans
        else:
            a = [random.randint(0, 1) for _ in range(5)]
            b = [random.randint(0, 1) for _ in range(5)]
            dist = sum(1 for i in range(5) if a[i] != b[i])
            a_str = "".join(str(bit) for bit in a)
            b_str = "".join(str(bit) for bit in b)
            q = _(
                f"Hamming distance between {a_str} and {b_str} = ?",
                f"Jarak Hamming antara {a_str} dan {b_str} = ?",
            )
            return q, str(dist), dist

    return None


__all__ = ["gen_question", "subtopics"]
