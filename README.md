# python サンプルコード

## M1 mac 向け環境のセットアップ

次のページを参考に Python3 をインストールする。

[M1 Mac で Python+OpenCV プログラミングできる環境を整える](https://qiita.com/uranishi/items/fba7e51a99d260a133cc)

python3 をインストールする。

```bash
$ brew install python3
```

インストールを確認。

```bash
$ which python3
/opt/homebrew/bin/python3
```

python3 の仮想環境を作成する。

```bash
$ ./script/setup-env.sh
```

カレントディレクトリに .venv ディレクトリが作成される。

以降、仮想環境上で作業するときは以下のスクリプトをターミナルを開くたびに実行して作業する。

```bash
$ ./script/active-env.sh
```

コマンドプロンプトが次のように (.venv) になっていることを確認する。

```bash
(.venv)
```

OpenCV をインストール。

```bash
(.venv) pip install numpy
(.venv) pip install opencv-python
```

main.py を実行。sample.jpeg 画像が表示されるウインドウが現れる。

```bash
(.venv) python3 main.py
```

終了はウインドウをアクティブにして何かキーを押下する。

## 参考

動画から静止画を切り出す方法は以下のページを参考に。

[Python, OpenCV で動画ファイルからフレームを切り出して保存](https://note.nkmk.me/python-opencv-video-to-still-image/)
