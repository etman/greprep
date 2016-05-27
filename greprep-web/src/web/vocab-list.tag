<vocab-list>
	<div class="row" each={ vocabs }>
		<div class="col-md-2">{ word }</div>
		<div class="col-md-6">{ definitions }</div>
		<div class="col-md-4">{ features }</div>
	</div>
	<script>
	var self = this;
	self.vocabs = [];
	
	$.get("/api/vocab", function(data) {
		console.info(data)
		self.vocabs = data;
		self.update();
	});
	</script>
</vocab-list>