const config = {
  schemaFile: 'http://localhost:8000/openapi.json',
  apiFile: "./emptyApi.ts",
  apiImport: "emptySplitApi",
  outputFile: "./apiStore.gen.ts",
  exportName: "api",
  useEnumType: true,
  hooks: true,
}
module.exports = config