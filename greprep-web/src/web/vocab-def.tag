<vocab-def>
<h1>{ dictWord.word }</h1>
<div class="row" each={ audio in dictWord.pronunciation }>
	<div class="col-md-12"><raw content="{ audio }"></raw></div>
</div>
<div each={ dictWord.definitions }>
	<div><h5>{ speech }</h5></div>
	<div class="row" each={ set }>
		<div class="col-md-12"><raw content="{ content }"></raw></div>
	</div>
</div>

<script>
	var self = this;
	console.info(opts);

	$.get("/api/vocab/" + opts.word, function(data) {
		console.info(data);
		self.dictWord = data;
		self.update();
	}, "json");
</script>
</vocab-def>