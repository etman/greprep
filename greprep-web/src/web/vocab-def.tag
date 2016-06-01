<vocab-def>
<h1>{ dictWord.word }</h1>
<div class="row" each="{ audio in dictWord.pronunciation }">
	<div class="col-md-12">
		<raw content="{ audio }"></raw>
	</div>
</div>
<ul class="nav nav-pills">
	<li role="presentation" class="active"><a href="#defTab"
		aria-controls="defTab" role="tab" data-toggle="tab">Definition</a></li>
	<li role="presentation"><a href="#exTab" aria-controls="exTab"
		role="tab" data-toggle="tab">Examples</a></li>
	<li role="presentation"><a href="#exSrcTab" aria-controls="exSrcTab"
		role="tab" data-toggle="tab">External Sources</a></li>
</ul>
<div class="tab-content">
	<div role="tabpanel" class="tab-pane active" id="defTab">
		<div each="{ dictWord.definitions }">
			<div>
				<h5>{ speech }</h5>
			</div>
			<div class="row" each="{ set }">
				<div class="col-md-12">
					<raw content="{ content }"></raw>
				</div>
			</div>
		</div>
	</div>
	<div role="tabpanel" class="tab-pane" id="exTab">
		<div each="{ dictWord.examples }">
			<div>
				<h5>{ title }</h5>
			</div>
			<div class="row voffset2" each="{ sentences }">
				<div class="col-md-12">
					<raw content="{ sentence }"></raw>
					<raw content="{ source }"></raw>
				</div>
			</div>
			<hr />
		</div>
	</div>
	<div role="tabpanel" class="tab-pane" id="exSrcTab">
		<div each="{ dictWord.externalSources }">
			<div>
				<h5>{ source }</h5>
			</div>
			<div class="row voffset2" each="{ definitions }">
				<div class="col-md-12">
					<div>
						<h5>{ speech }</h5>
					</div>
					<div class="row" each="{ set }">
						<div class="col-md-12">
							<raw content="{ content }"></raw>
						</div>
					</div>
				</div>
			</div>
			<hr />
		</div>
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
</script> <br />
</vocab-def>