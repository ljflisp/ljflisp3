const { XMLParser, XMLBuilder, XMLValidator} = require('fast-xml-parser');

const parser = new XMLParser({
	ignoreDeclaration: true,
	ignoreAttributes: true,
});

const builder = new XMLBuilder({
	format: true,
	indentBy: '  ',
});

const XML = {
	parse: function(str) { return parser.parse(str) },
	stringify: function(xml) { return `<?xml version="1.0" encoding="UTF-8" ?>\n${builder.build(xml)}` },
}

const Ajv = require('ajv')
const ajv = new Ajv();

const schema = require('../schema.js');
const data = XML.parse(require('node:fs').readFileSync('data.xml', 'utf-8'));

if(schema !== null) {
	const validate = ajv.compile(schema);
	const valid = validate(data)
	
	if (!valid) console.error('Schema Errors', validate.errors);
	else console.log('XML is valid.');
} else {
	console.clear();
	console.log(XML.stringify(data).trim());
}