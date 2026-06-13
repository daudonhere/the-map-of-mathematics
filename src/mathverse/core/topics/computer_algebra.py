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
                "Dekripsi: geser kembali ke arah sebaliknya sebanyak kunci yang sama.\n"
                "Kriptografi modern menggunakan kunci publik dan privat (RSA) — "
                "satu kunci untuk enkripsi, kunci lain untuk dekripsi.\n"
                "Enkripsi RSA: pangkatkan plainteks m dengan e modulo n — keamanan "
                "bergantung pada sulitnya memfaktorkan bilangan besar.\n"
                "Dekripsi RSA: pangkatkan cipherteks c dengan d modulo n — hanya "
                "pemilik kunci privat d yang bisa memulihkan pesan asli.\n"
                "Hash functions: menghasilkan sidik jari digital dari data, tidak dapat dibalik.\n"
                "SHA-256 menghasilkan digest 256 bit (64 karakter hex) — "
                "perubahan kecil pada input mengubah output sepenuhnya.\n"
                "Output dengan panjang tetap (256 bit) berarti input berapa pun "
                "ukurannya menghasilkan hash berukuran sama."
            ),
            "en": (
                "Caesar cipher: shift each letter by n positions — the simplest cipher.\n"
                "With key 3, A\u2192D, B\u2192E, C\u2192F, ... Z\u2192C — shift cipher.\n"
                "Decryption: shift back by the same key amount.\n"
                "Modern cryptography uses public and private keys (RSA) — "
                "one key for encryption, another for decryption.\n"
                "RSA encryption raises the plaintext message m to the power e modulo n — "
                "the security relies on the difficulty of factoring large numbers.\n"
                "RSA decryption raises the ciphertext c to the power d modulo n — "
                "only the holder of the private key d can recover the original message.\n"
                "Hash functions: produce a digital fingerprint of data, irreversible.\n"
                "SHA-256 produces a 256-bit (64 hex character) digest — "
                "even a tiny change in input completely changes the output.\n"
                "The fixed-length output (256 bits) means any input, regardless "
                "of size, yields an identically-sized hash."
            ),
        },
        examples={
            "id": [
                "Caesar cipher (kunci=3):",
                "  HELLO \u2192 KHOOR",
                "  (H\u2192K, E\u2192H, L\u2192O, L\u2192O, O\u2192R)",
                "",
                "RSA: kunci publik (n, e), kunci privat (n, d)",
                "  Enkripsi: c = m^e mod n",
                "  Dekripsi: m = c^d mod n",
                "",
                "Hash SHA-256:",
                "  'Hello' \u2192 185f8db3...",
                "  (panjang tetap 256 bit)",
            ],
            "en": [
                "Caesar cipher (key=3):",
                "  HELLO \u2192 KHOOR",
                "  (H\u2192K, E\u2192H, L\u2192O, L\u2192O, O\u2192R)",
                "",
                "RSA: public key (n, e), private key (n, d)",
                "  Encryption: c = m^e mod n",
                "  Decryption: m = c^d mod n",
                "",
                "SHA-256 hash:",
                "  'Hello' \u2192 185f8db3...",
                "  (fixed length 256 bits)",
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
                "Kode biner: setiap pesan dikodekan sebagai urutan 0 dan 1 — "
                "fondasi semua komunikasi digital.\n"
                "Parity bit: tambahkan bit ekstra agar jumlah bit 1 genap "
                "(even parity) — mendeteksi kesalahan satu bit.\n"
                "Setelah parity bit ditambahkan, codeword memiliki jumlah "
                "bit 1 genap, memenuhi properti parity.\n"
                "Jarak Hamming mengukur berapa banyak posisi bit yang berbeda "
                "antara dua codeword — jarak minimum menentukan kemampuan koreksi error.\n"
                "Jarak Hamming 2 berarti kedua kode berbeda tepat di 2 posisi "
                "— cukup untuk mendeteksi error.\n"
                "Jarak Hamming 4 berarti kode berbeda di 4 posisi — memberikan "
                "kemampuan deteksi dan koreksi yang lebih besar.\n"
                "Hamming(7,4) adalah kode koreksi error yang mengkodekan "
                "4 bit data menjadi codeword 7 bit.\n"
                "4 bit data digabungkan dengan 3 bit parity untuk "
                "menghasilkan codeword 7 bit penuh.\n"
                "Bit parity tambahan menyediakan redundansi yang memungkinkan "
                "penerima mendeteksi dan memperbaiki error satu bit."
            ),
            "en": (
                "Binary code: every message is encoded as a sequence of 0s and 1s "
                "— the foundation of all digital communication.\n"
                "Parity bit: add an extra bit to make the total number of 1s even "
                "(even parity) — detects single-bit errors.\n"
                "After adding the parity bit, the codeword now has an even number "
                "of 1s, confirming the parity property.\n"
                "Hamming distance measures how many bit positions differ between two "
                "codewords — the minimum distance determines error correction capability.\n"
                "A Hamming distance of 2 means the two codes differ in exactly 2 "
                "positions — enough to detect errors.\n"
                "A Hamming distance of 4 means the codes differ in 4 positions — "
                "providing greater error detection and correction ability.\n"
                "Hamming(7,4) is an error-correcting code that encodes 4 data bits "
                "into 7-bit codewords.\n"
                "The 4 data bits are combined with 3 parity bits to produce "
                "the full 7-bit codeword.\n"
                "The extra parity bits provide redundancy that allows the receiver "
                "to detect and correct single-bit errors."
            ),
        },
        examples={
            "id": [
                "Parity bit (even parity):",
                "  1011: 3 bit 1 (ganjil) \u2192 tambah 1",
                "  menjadi 10111 (4 bit 1, genap)",
                "",
                "Hamming distance:",
                "  1010 dan 1001 berbeda di 2 bit \u2192 d=2",
                "  1111 dan 0000 berbeda di 4 bit \u2192 d=4",
                "",
                "Hamming(7,4):",
                "  Data 1010 \u2192 codeword 1010010",
                "  (4 data + 3 parity = 7 bit)",
            ],
            "en": [
                "Parity bit (even parity):",
                "  1011: 3 ones (odd) \u2192 append 1",
                "  becomes 10111 (4 ones, even)",
                "",
                "Hamming distance:",
                "  1010 and 1001 differ in 2 bits \u2192 d=2",
                "  1111 and 0000 differ in 4 bits \u2192 d=4",
                "",
                "Hamming(7,4):",
                "  Data 1010 \u2192 codeword 1010010",
                "  (4 data + 3 parity = 7 bits)",
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
                "dari blok sebelumnya, menghubungkannya dalam rantai yang aman.\n"
                "Blok 1 tidak memiliki blok sebelumnya (HashPrev=0), sehingga "
                "disebut genesis block — fondasi seluruh rantai.\n"
                "Blok 2 menyimpan hash dari Blok 1, menciptakan tautan yang "
                "tidak dapat diubah — jika Blok 1 diubah, hash yang disimpan "
                "Blok 2 tidak akan cocok.\n"
                "Proof of work adalah mekanisme konsensus di mana penambang "
                "bersaing memecahkan teka-teki komputasi.\n"
                "Teka-teki membutuhkan pencarian nonce sehingga hash blok "
                "dimulai dengan sejumlah nol di depan.\n"
                "Hash yang valid seperti 0000a3f5... sangat langka dan "
                "membutuhkan banyak percobaan — ini membuat manipulasi "
                "mahal secara komputasi.\n"
                "Merkle tree merangkum semua transaksi dalam blok secara "
                "efisien menggunakan pohon hash.\n"
                "Root Merkle dihitung dengan menggabungkan hash berpasangan "
                "dari hash transaksi hingga tersisa satu hash.\n"
                "Untuk memverifikasi transaksi dalam blok, cukup root Merkle "
                "dan bukti cabang — tidak perlu semua transaksi."
            ),
            "en": (
                "Each block in a blockchain contains data, a timestamp, and the hash "
                "of the previous block, linking them into a secure chain.\n"
                "Block 1 has no previous block (HashPrev=0), so it is the genesis "
                "block — the foundation of the entire chain.\n"
                "Block 2 stores the hash of Block 1, creating an immutable link — "
                "if Block 1 is altered, Block 2's stored hash would no longer match.\n"
                "Proof of work is a consensus mechanism where miners compete to "
                "solve a computational puzzle.\n"
                "The puzzle requires finding a nonce such that the block's hash "
                "begins with a specified number of leading zeros.\n"
                "A valid hash like 0000a3f5... is extremely rare and requires "
                "many attempts to find — this makes tampering computationally expensive.\n"
                "A Merkle tree efficiently summarizes all transactions in a block "
                "using a tree of hashes.\n"
                "The Merkle root is computed by repeatedly hashing pairs of "
                "transaction hashes until a single hash remains.\n"
                "To verify a transaction belongs in a block, only the Merkle root "
                "and a small branch proof are needed — not all transactions."
            ),
        },
        examples={
            "id": [
                "Struktur blok:",
                "  Blok 1: [Data1 | Timestamp | HashPrev=0 | Nonce | Hash]",
                "  Blok 2: [Data2 | Timestamp | HashPrev=Hash1 | Nonce | Hash]",
                "",
                "Proof of work (Bitcoin):",
                "  Cari nonce sehingga hash mulai dengan 0000...",
                "  Contoh: hash(blok + nonce) = 0000a3f5...",
                "",
                "Merkle tree:",
                "  Root hash dihitung dari hash semua transaksi",
                "  Verifikasi: cukup punya root + bukti cabang",
            ],
            "en": [
                "Block structure:",
                "  Block 1: [Data1 | Timestamp | HashPrev=0 | Nonce | Hash]",
                "  Block 2: [Data2 | Timestamp | HashPrev=Hash1 | Nonce | Hash]",
                "",
                "Proof of work (Bitcoin):",
                "  Find nonce so hash starts with 0000...",
                "  Example: hash(block + nonce) = 0000a3f5...",
                "",
                "Merkle tree:",
                "  Root hash computed from all transaction hashes",
                "  Verification: just need root + branch proof",
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
                "Repetition code: kirim setiap bit 3 kali (111 untuk 1, 000 untuk 0) "
                "— jika satu bit error, mayoritas menang.\n"
                "Enkoding: bit data asli 1 dikirim sebagai tiga salinan (111) "
                "untuk redundansi.\n"
                "Dekoding mayoritas: meskipun bit tengah rusak (101), "
                "dua bit 1 lainnya menunjukkan nilai yang benar adalah 1.\n"
                "Dengan 2 dari 3 bit bernilai 1, aturan mayoritas menghasilkan "
                "1 dengan benar — satu bit error dapat ditoleransi.\n"
                "Hamming(7,4) adalah kode koreksi error linear yang dapat "
                "mendeteksi dan memperbaiki error satu bit.\n"
                "Codeword yang diterima 1010110 berbeda dari 1010010 yang "
                "benar di satu posisi — menunjukkan adanya error.\n"
                "Dengan menganalisis bit parity, penerima mengidentifikasi "
                "bit ke-5 sebagai error dan membaliknya ke nilai yang benar 0.\n"
                "Kode Reed-Solomon banyak digunakan dalam QR code, CD, dan "
                "DVD untuk melindungi dari burst error.\n"
                "Kode Reed-Solomon sangat tangguh sehingga QR code tetap "
                "terbaca bahkan dengan hingga 30% kerusakan."
            ),
            "en": (
                "Repetition code: send each bit 3 times (111 for 1, 000 for 0) "
                "— if one bit is wrong, majority wins.\n"
                "Encoding: the original data bit 1 is transmitted as three "
                "copies (111) for redundancy.\n"
                "Majority decoding: even though the middle bit was "
                "corrupted (101), the other two 1s indicate the correct value is 1.\n"
                "With 2 out of 3 bits being 1, the majority rule correctly "
                "outputs 1 — one bit error can be tolerated.\n"
                "Hamming(7,4) is a linear error-correcting code that can "
                "detect and correct single-bit errors.\n"
                "The received codeword 1010110 differs from the correct "
                "1010010 at one position — indicating an error.\n"
                "By analyzing parity bits, the receiver identifies bit 5 "
                "as the error and flips it back to the correct value of 0.\n"
                "Reed-Solomon codes are widely used in QR codes, CDs, and "
                "DVDs to protect against burst errors.\n"
                "Reed-Solomon codes are so robust that QR codes remain "
                "readable even with up to 30% of the code damaged."
            ),
        },
        examples={
            "id": [
                "Repetition code (r=3):",
                "  Data: 1 \u2192 dikirim 111",
                "  Terima 101 \u2192 mayoritas 1 \u2192 perbaiki ke 1",
                "  (2 dari 3 bit adalah 1 \u2192 output 1)",
                "",
                "Hamming(7,4) dapat memperbaiki 1 error:",
                "  Codeword 1010010 diterima 1010110",
                "  \u2192 error di bit ke-5 \u2192 perbaiki ke 0",
                "",
                "QR code menggunakan Reed-Solomon:",
                "  hingga ~30% kerusakan masih dapat dibaca",
            ],
            "en": [
                "Repetition code (r=3):",
                "  Data: 1 \u2192 send 111",
                "  Receive 101 \u2192 majority 1 \u2192 correct to 1",
                "  (2 out of 3 bits are 1 \u2192 output 1)",
                "",
                "Hamming(7,4) can correct 1 error:",
                "  Codeword 1010010 received as 1010110",
                "  \u2192 error at bit 5 \u2192 correct to 0",
                "",
                "QR codes use Reed-Solomon:",
                "  up to ~30% damage still readable",
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
