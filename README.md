# DSA-Solutions

Algoritma ve Veri Yapıları çözümleri koleksiyonu — **Python 3** ile yazılmış, LeetCode tabanlı çözümler.

Her dosya; problem açıklaması, yaklaşım notu, zaman/uzay karmaşıklığı analizi ve örnek input/output içerir. Ayrıca her dosya doğrudan `python <dosya>.py` ile çalıştırılabilir (örnek test senaryoları `__main__` bloğunda).

## 📂 Kategoriler

- [arrays/](arrays/) — Diziler
- [strings/](strings/) — String işleme
- [linked-lists/](linked-lists/) — Bağlı listeler
- [trees/](trees/) — Ağaçlar
- [graphs/](graphs/) — Çizgeler
- [dynamic-programming/](dynamic-programming/) — Dinamik programlama
- [sorting/](sorting/) — Sıralama algoritmaları
- [binary-search/](binary-search/) — İkili arama

## 📋 Tüm Çözümler

| # | Problem | Kategori | Zorluk | Çözüm |
|---|---------|----------|--------|-------|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Arrays | 🟢 Easy | [link](arrays/two_sum.py) |
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Arrays | 🟢 Easy | [link](arrays/best_time_to_buy_sell_stock.py) |
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Arrays | 🟢 Easy | [link](arrays/contains_duplicate.py) |
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Arrays | 🟡 Medium | [link](arrays/product_of_array_except_self.py) |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Strings | 🟢 Easy | [link](strings/valid_anagram.py) |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Strings | 🟢 Easy | [link](strings/valid_palindrome.py) |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Strings | 🟡 Medium | [link](strings/longest_substring_without_repeating.py) |
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Linked Lists | 🟢 Easy | [link](linked-lists/reverse_linked_list.py) |
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Linked Lists | 🟢 Easy | [link](linked-lists/merge_two_sorted_lists.py) |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Linked Lists | 🟢 Easy | [link](linked-lists/linked_list_cycle.py) |
| 226 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Trees | 🟢 Easy | [link](trees/invert_binary_tree.py) |
| 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Trees | 🟢 Easy | [link](trees/maximum_depth_binary_tree.py) |
| 100 | [Same Tree](https://leetcode.com/problems/same-tree/) | Trees | 🟢 Easy | [link](trees/same_tree.py) |
| 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | Graphs | 🟡 Medium | [link](graphs/number_of_islands.py) |
| 133 | [Clone Graph](https://leetcode.com/problems/clone-graph/) | Graphs | 🟡 Medium | [link](graphs/clone_graph.py) |
| 70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | DP | 🟢 Easy | [link](dynamic-programming/climbing_stairs.py) |
| 198 | [House Robber](https://leetcode.com/problems/house-robber/) | DP | 🟡 Medium | [link](dynamic-programming/house_robber.py) |
| 322 | [Coin Change](https://leetcode.com/problems/coin-change/) | DP | 🟡 Medium | [link](dynamic-programming/coin_change.py) |
| - | Merge Sort | Sorting | 🟡 Medium | [link](sorting/merge_sort.py) |
| - | Quick Sort | Sorting | 🟡 Medium | [link](sorting/quick_sort.py) |
| 704 | [Binary Search](https://leetcode.com/problems/binary-search/) | Binary Search | 🟢 Easy | [link](binary-search/binary_search.py) |
| 33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Binary Search | 🟡 Medium | [link](binary-search/search_in_rotated_sorted_array.py) |

**Toplam:** 22 çözüm · 13 Easy · 9 Medium

## 🚀 Kullanım

```bash
# Çözümü çalıştırmak için:
python arrays/two_sum.py
python dynamic-programming/coin_change.py
```

Python 3.8+ önerilir. Harici bağımlılık yok — sadece standart kütüphane.

## 🤝 Katkıda Bulunma

Pull request ve yeni çözüm önerileri memnuniyetle karşılanır. Yeni bir çözüm eklerken:

1. Uygun kategori klasörüne dosyayı ekle (snake_case isim).
2. Dosyanın başına problem açıklaması, yaklaşım, complexity analizi ve örnek ekle.
3. `__main__` bloğunda en az bir örnek test koş.
4. Kategori README'sini ve ana README tablosunu güncelle.

## 📄 Lisans

MIT — ayrıntılar için [LICENSE](LICENSE) dosyasına bakınız.
