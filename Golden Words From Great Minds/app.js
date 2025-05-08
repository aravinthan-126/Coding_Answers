window.onload = function () {
  loadQuotes();
};

function loadQuotes() {
  const quotes = JSON.parse(localStorage.getItem("quotes")) || [];
  const quotesContainer = document.getElementById("quotes");
  quotesContainer.innerHTML = "";

  quotes.forEach((quote, index) => {
    const quoteElement = document.createElement("div");
    quoteElement.classList.add("quote-box");

    quoteElement.innerHTML = `
      <p>"${quote.text}"</p>
      <p>- ${quote.author}</p>
      <p><strong>Category:</strong> ${quote.category}</p>
      <button class="delete-btn" onclick="deleteQuote(${index})">Delete</button>
    `;

    quotesContainer.appendChild(quoteElement);
  });
}

function deleteQuote(index) {
  let quotes = JSON.parse(localStorage.getItem("quotes")) || [];
  quotes.splice(index, 1); // remove the quote at the index
  localStorage.setItem("quotes", JSON.stringify(quotes));
  loadQuotes(); // reload the list
}

document.getElementById("quoteForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const quoteText = document.getElementById("quoteText").value.trim();
  const author = document.getElementById("author").value.trim();
  const category = document.getElementById("category").value.trim();
  
  if (quoteText && author && category) {
    const newQuote = {
      text: quoteText,
      author: author,
      category: category,
    };

    const quotes = JSON.parse(localStorage.getItem("quotes")) || [];
    quotes.push(newQuote);
    localStorage.setItem("quotes", JSON.stringify(quotes));

    document.getElementById("quoteText").value = "";
    document.getElementById("author").value = "";
    document.getElementById("category").value = "";

    loadQuotes();
  } else {
    alert("Please fill in all fields!");
  }
});
