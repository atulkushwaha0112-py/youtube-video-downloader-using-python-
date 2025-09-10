<h1>🎯 Python Project: YouTube Video Downloader</h1>

<p>
A <strong>Python project</strong> for downloading YouTube videos using 
<a href="https://pypi.org/project/pytubefix/">pytubefix</a>.  
This repository includes <strong>two versions</strong>:
</p>

<ol>
  <li><strong>Basic Downloader</strong> → Beginner-friendly (up to 720p, video + audio in one file).</li>
  <li><strong>Advanced Downloader</strong> → High-quality (1080p, 1440p, 4K) with video/audio merging using 
    <a href="https://pypi.org/project/moviepy/">moviepy</a>.
  </li>
</ol>

<hr />

<h2>✅ 1. Basic YouTube Downloader</h2>

<h3>📌 Overview</h3>
<ul>
  <li>Takes a YouTube video URL</li>
  <li>Shows video details (title, author, duration)</li>
  <li>Downloads the <strong>highest progressive stream</strong> (video + audio combined, up to 360p/720p)</li>
</ul>
<p>⚠️ Use the <strong>Advanced Downloader</strong> for Full HD or 4K videos.</p>


<h3>🛠️ Prerequisites</h3>
<p>First, install the <code>pytubefix</code> library using pip:</p>
<pre><code class="language-bash">pip install pytubefix</code></pre>


<hr />

<h2>📥 2. Advanced YouTube Downloader (Video + Audio Merge)</h2>

<h3>📌 Why Advanced?</h3>
<p>
YouTube separates <strong>video</strong> and <strong>audio</strong> streams for 1080p, 1440p, and 4K.  
The advanced script downloads them separately and merges into a single MP4 file.
</p>

<h3>🔧 Installation</h3>

<hr />



 <h2><i class="fa-brands fa-python"></i> Step 1: Install Required Python Modules</h2>
  <p>Make sure you have Python 3.8+ installed. Then open your terminal (or command prompt) and run:</p>
  <pre><code class="language-bash">
pip install pytubefix 
  </code></pre>
  <p>This will install:</p>
  <ul>
    <li><strong>pytubefix</strong> → a reliable fork of pytube for downloading YouTube videos.</li>
  </ul>
  <hr>
  
  <pre><code class="language-bash">
pip install moviepy==1.0.3
  </code></pre>
  <p>This will install:</p>
  <ul>
    <li><strong>moviepy</strong> → to merge video & audio streams into a final MP4.</li>
    <a href="https://onlypython01.blogspot.com/2025/08/moviepy-installation-in-python.html" target="_blank" 
     style="background:#2563eb; color:#fff; padding:12px 22px; border-radius:8px; 
            text-decoration:none; font-size:18px; font-weight:bold; 
            display:inline-block; box-shadow:0 4px 8px rgba(0,0,0,0.2);">
    📘 Get Full MoviePy Installation Tutorial
  </a>
  </ul>
<hr>



<h2>💡 Tips & Improvements</h2>
<ul>
  <li>Keep <code>pytubefix</code> updated:
    <pre><code class="language-bash">pip install -U pytubefix</code></pre>
  </li>
  <li>Modify resolution preferences in the script for <strong>4K/2160p</strong>.</li>
  <li>Adjust bitrate for smaller file sizes.</li>
  <li>Wrap the downloader into a <strong>function</strong> or <strong>GUI app</strong> (Tkinter, PyQt).</li>
</ul>
<hr />

  


<h2>🚀 Conclusion</h2>
<ul>
  <li><strong>Basic Downloader</strong> → Great for beginners (easy setup, up to 720p).</li>
  <li><strong>Advanced Downloader</strong> → Best for Full HD & 4K with audio merging.</li>
</ul>

<p>
With Python, you get <strong>full control</strong> over YouTube downloads — no online tools required. 🎉
</p>
